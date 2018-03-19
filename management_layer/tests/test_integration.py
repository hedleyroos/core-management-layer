import json
import jsonschema
import logging
import os
import socket
import subprocess
import time
import uuid
from aiohttp import web
from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
from apitools.datagenerator import DataGenerator
from collections import namedtuple
from unittest.mock import patch
from parameterized import parameterized

import access_control
import authentication_service
import user_data_store
from user_data_store import UserDataApi
from management_layer.api import schemas
from management_layer.api.urls import add_routes

LOGGER = logging.getLogger(__name__)
DATA_GENERATOR = DataGenerator()
# The data generated drops object parameters even if they are required.
# the workaround for now is to set the value below.
DATA_GENERATOR.not_required_probability = 1.0

# Mocked service ports
ACCESS_CONTROL_PORT = 60000
AUTHENTICATION_SERVICE_PORT = 60001
USER_DATA_STORE_PORT = 60002


_MOCKED_ACCESS_CONTROL_API = None
_MOCKED_AUTHENTICATION_SERVICE_API = None
_MOCKED_USER_DATA_STORE_API = None

_PRISM_COMMAND = "./prism run --validate --mockDynamic -s {}/{} -p {}"

_TOTAL_COUNT_HEADER = "X-Total-Count"

Resource = namedtuple("Resource", [
    "num_identifying_parts", "schema", "create_schema", "update_schema"
])
# A list of resources. Used to parameterise tests.
RESOURCES = {
    "adminnotes": Resource(1, schemas.admin_note, schemas.admin_note_create, schemas.admin_note_update),
    "domains": Resource(1, schemas.domain, schemas.domain_create, schemas.domain_update),
    "domainroles": Resource(2, schemas.domain_role, schemas.domain_role_create, schemas.domain_role_update),
    # TODO: Uncomment when these are implemented
    # "invitations": Resource(1, schemas.invitation, schemas.invitation_create, schemas.invitation_update),
    # "invitationdomainroles": Resource(3, schemas.invitation_domain_role, schemas.invitation_domain_role_create, None),
    # "invitationsiteroles": Resource(3, schemas.invitation_site_role, schemas.invitation_site_role_create, None),
    "permissions": Resource(1, schemas.permission, schemas.permission_create, schemas.permission_update),
    "resources": Resource(1, schemas.resource, schemas.resource_create, schemas.resource_update),
    "roles": Resource(1, schemas.role, schemas.role_create, schemas.role_update),
    "roleresourcepermissions": Resource(3, schemas.role_resource_permission, schemas.role_resource_permission_create, None),
    "sites": Resource(1, schemas.site, schemas.site_create, schemas.site_update),
    "sitedataschemas": Resource(1, schemas.site_data_schema, schemas.site_data_schema_create, schemas.site_data_schema_update),
    "siteroles": Resource(2, schemas.site_role, schemas.site_role_create, schemas.site_role_update),
    "userdomainroles": Resource(3, schemas.user_domain_role, schemas.user_domain_role_create, None),
    "usersitedata": Resource(2, schemas.user_site_data, schemas.user_site_data_create, schemas.user_site_data_update),
    "usersiteroles": Resource(3, schemas.user_site_role, schemas.user_site_role_create, None),
    "clients": Resource(1, schemas.client, None, None),
    "users": Resource(1, schemas.user, None, schemas.user_update)
}
SKIP_DELETE_TESTS_FOR = ["clients"]


def wait_for_server(ip, port):
    """
    Wait until a server is
    :param ip: The IP address to connect to
    :param port: The port to connect to
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            s.connect((ip, int(port)))
            s.shutdown(2)
            break
        except Exception:
            time.sleep(1)


def setUpModule():
    """
    This function is used to launch mocked backend APIs.
    """
    workdir = os.getenv("TRAVIS_BUILD_DIR", ".")
    global _MOCKED_ACCESS_CONTROL_API
    cmd = _PRISM_COMMAND.format(
        workdir,  "swagger/access_control.yml", ACCESS_CONTROL_PORT
    )
    LOGGER.info("Starting mock server using: {}".format(cmd))
    _MOCKED_ACCESS_CONTROL_API = subprocess.Popen(cmd.split())

    global _MOCKED_AUTHENTICATION_SERVICE_API
    cmd = _PRISM_COMMAND.format(
        workdir, "swagger/authentication_service.yml", AUTHENTICATION_SERVICE_PORT
    )
    LOGGER.info("Starting mock server using: {}".format(cmd))
    _MOCKED_AUTHENTICATION_SERVICE_API = subprocess.Popen(cmd.split())

    global _MOCKED_USER_DATA_STORE_API
    cmd = _PRISM_COMMAND.format(
        workdir, "swagger/user_data_store.yml", USER_DATA_STORE_PORT
    )
    LOGGER.info("Starting mock server using: {}".format(cmd))
    _MOCKED_USER_DATA_STORE_API = subprocess.Popen(cmd.split())

    for port in [ACCESS_CONTROL_PORT, AUTHENTICATION_SERVICE_PORT, USER_DATA_STORE_PORT]:
        wait_for_server("127.0.0.1", port)


def tearDownModule():
    """
    Stop the mocked APIs
    """
    _MOCKED_ACCESS_CONTROL_API.terminate()
    _MOCKED_AUTHENTICATION_SERVICE_API.terminate()
    _MOCKED_USER_DATA_STORE_API.terminate()


def get_test_data(schema):
    """
    The utility used to generate test data is not feature-complete.
    This function is an attempt to fix the gotchas.
    :param schema:
    :return:
    """
    data = DATA_GENERATOR.random_value(schema)
    # Overwrite fields that expect a UUID
    for field in ["user_id", "creator_id", "invitation_id", "client_id"]:
        if field in data:
            data[field] = str(uuid.uuid1())
    # Overwrite fields that expect a datetime
    for field in ["consented_at", "last_login"]:
        if field in data:
            data[field] = "2000-01-01T00:00:00Z"

    # Overwrite fields that expect a datetime
    for field in ["birth_date"]:
        if field in data:
            data[field] = "2000-01-01"

    if "urn" in data:
        data["urn"] = "urn:ge:test:resource"

    if "name" in data:
        data["name"] = data["name"][:30]

    # URL fields
    for field in ["avatar"]:
        if field in data:
            data[field] = "http://example.com/"

    # Email fields
    for field in ["email"]:
        if field in data:
            data[field] = "me@example.com"

    return data


def validate_response_schema(response_body, schema):
    try:
        jsonschema.validate(response_body, schema)
    except jsonschema.ValidationError:
        print(response_body)
        raise


def clean_response_data(data):
    if type(data) is list:
        return [clean_response_data(d) for d in data]

    if "urn" in data:
        data["urn"] = "urn:ge:this:is:a:test"

    for k, v in data.items():
        if v is None:
            print("Removing field {} from response because it is None")

    return {k: v for k, v in data.items() if v is not None}


class ExampleTestCase(AioHTTPTestCase):
    """
    This is the example test case as provided in the aiohttp documentation:
    https://docs.aiohttp.org/en/stable/testing.html
    """
    async def get_application(self):
        """
        Set up the application used by the tests
        :return:
        """
        async def hello(request):
            return web.Response(text='Hello, world')

        app = web.Application(loop=self.loop)
        app.router.add_get('/', hello)
        return app

    # the unittest_run_loop decorator can be used in tandem with
    # the AioHTTPTestCase to simplify running
    # tests that are asynchronous
    @unittest_run_loop
    async def test_example(self):
        request = await self.client.request("GET", "/")
        assert request.status == 200
        text = await request.text()
        assert "Hello, world" in text

    # a vanilla example
    def test_example_vanilla(self):
        async def test_get_route():
            url = "/"
            resp = await self.client.request("GET", url)
            assert resp.status == 200
            text = await resp.text()
            assert "Hello, world" in text

        self.loop.run_until_complete(test_get_route())


class IntegrationTest(AioHTTPTestCase):
    """
    Test functionality in integration.py
    """

    async def assertStatus(self, response, status):
        """
        Convenience function that will dump the response body in the event
        that an unexpected response code is received.
        :param response: The response
        :param status: The expected status
        """
        if response.status != status:
            body = await response.text()
            print(body)

        self.assertEqual(response.status, status)

    async def get_application(self):
        """
        Set up the application used by the tests
        :return:
        """
        app = web.Application(loop=self.loop)

        user_data_store_configuration = user_data_store.configuration.Configuration()
        user_data_store_configuration.host = "http://localhost:{}/api/v1".format(USER_DATA_STORE_PORT)
        app["user_data_api"] = UserDataApi(
            api_client=user_data_store.ApiClient(
                configuration=user_data_store_configuration
            )
        )

        access_control_configuration = access_control.configuration.Configuration()
        access_control_configuration.host = "http://localhost:{}/api/v1".format(ACCESS_CONTROL_PORT)
        app["access_control_api"] = access_control.api.AccessControlApi(
            api_client=access_control.ApiClient(
                configuration=access_control_configuration
            )
        )

        # Operational API is a part of access control. It was split out by the
        # swagger generator due to its tag. Thus allowing it to use the same
        # client and config as access_control.
        app["operational_api"] = access_control.api.OperationalApi(
            api_client=access_control.ApiClient(
                configuration=access_control_configuration
            )
        )

        authentication_service_configuration = authentication_service.configuration.Configuration()
        authentication_service_configuration.host = "http://localhost:{}/api/v1".format(AUTHENTICATION_SERVICE_PORT)
        app["authentication_service_api"] = authentication_service.api.AuthenticationApi(
            api_client=authentication_service.ApiClient(
                configuration=authentication_service_configuration
            )
        )


        add_routes(app, with_ui=False)
        return app

    @parameterized.expand([
        (resource, info) for resource, info in RESOURCES.items()
    ])
    @unittest_run_loop
    async def test_list(self, resource, info):
        # Default call
        response = await self.client.get("/{}".format(resource))
        await self.assertStatus(response, 200)
        response_body = await response.json()
        response_body = clean_response_data(response_body)
        validate_response_schema(response_body, {"type": "array", "items": info.schema})
        self.assertIn(_TOTAL_COUNT_HEADER, response.headers)

        # With arguments
        response = await self.client.get("/{}?offset=1&limit=10".format(resource))
        await self.assertStatus(response, 200)
        response_body = await response.json()
        response_body = clean_response_data(response_body)
        validate_response_schema(response_body, {"type": "array", "items": info.schema})
        self.assertIn(_TOTAL_COUNT_HEADER, response.headers)

        # With arguments
        response = await self.client.get("/{}?foo=bar".format(resource))
        await self.assertStatus(response, 200)
        response_body = await response.json()
        response_body = clean_response_data(response_body)
        validate_response_schema(response_body, {"type": "array", "items": info.schema})
        self.assertIn(_TOTAL_COUNT_HEADER, response.headers)

        # With bad arguments
        response = await self.client.get("/{}?offset=a".format(resource))
        await self.assertStatus(response, 400)

        # Quick check that CORS is working
        response = await self.client.request(
            "OPTIONS", "/{}?offset=1&limit=10".format(resource),
            headers={
                "Origin": "http://foo.bar",
                "Access-Control-Request-Method": "GET"
            }
        )
        await self.assertStatus(response, 200)

        response = await self.client.request(
            "OPTIONS", "/{}?offset=1&limit=10".format(resource),
            headers={
                "Origin": "http://foo.bar",
                "Access-Control-Request-Method": "DELETE"
            }
        )
        await self.assertStatus(response, 403)

    @parameterized.expand([
        (resource, info) for resource, info in RESOURCES.items()
    ])
    @unittest_run_loop
    async def test_create(self, resource, info):
        if info.create_schema is None:  # Some resources cannot be created
            return

        data = get_test_data(info.create_schema)
        response = await self.client.post("/{}".format(resource), data=json.dumps(data))
        await self.assertStatus(response, 201)
        response_body = await response.json()
        response_body = clean_response_data(response_body)
        validate_response_schema(response_body, info.schema)

        # Quick check that CORS is working
        response = await self.client.request(
            "OPTIONS", "/{}".format(resource),
            headers={
                "Origin": "http://foo.bar",
                "Access-Control-Request-Method": "POST"
            }
        )
        await self.assertStatus(response, 200)

    @parameterized.expand([
        (resource, info) for resource, info in RESOURCES.items()
        if resource not in SKIP_DELETE_TESTS_FOR
    ])
    @unittest_run_loop
    async def test_delete(self, resource, info):
        response = await self.client.delete("/{}{}".format(
            resource, "/1" * info.num_identifying_parts)
        )
        await self.assertStatus(response, 204)

        # Quick check that CORS is working
        response = await self.client.request(
            "OPTIONS", "/{}{}".format(resource, "/1" * info.num_identifying_parts),
            headers={
                "Origin": "http://foo.bar",
                "Access-Control-Request-Method": "DELETE"
            }
        )
        await self.assertStatus(response, 200)

    @parameterized.expand([
        (resource, info) for resource, info in RESOURCES.items()
    ])
    @unittest_run_loop
    async def test_read(self, resource, info):
        response = await self.client.get("/{}{}".format(
            resource, "/1" * info.num_identifying_parts)
        )
        await self.assertStatus(response, 200)
        response_body = await response.json()
        response_body = clean_response_data(response_body)
        validate_response_schema(response_body, info.schema)

        # Quick check that CORS is working
        response = await self.client.request(
            "OPTIONS", "/{}{}".format(resource, "/1" * info.num_identifying_parts),
            headers={
                "Origin": "http://foo.bar",
                "Access-Control-Request-Method": "GET"
            }
        )
        await self.assertStatus(response, 200)

    @parameterized.expand([
        (resource, info) for resource, info in RESOURCES.items()
    ])
    @unittest_run_loop
    async def test_update(self, resource, info):
        if info.update_schema is None:  # Some resources cannot be updated
            return

        data = get_test_data(info.update_schema)
        response = await self.client.put(
            "/{}{}".format(resource, "/1" * info.num_identifying_parts),
            data=json.dumps(data)
        )
        await self.assertStatus(response, 200)
        response_body = await response.json()
        response_body = clean_response_data(response_body)
        validate_response_schema(response_body, info.schema)

        # Quick check that CORS is working
        response = await self.client.request(
            "OPTIONS", "/{}{}".format(resource, "/1" * info.num_identifying_parts),
            headers={
                "Origin": "http://foo.bar",
                "Access-Control-Request-Method": "PUT"
            }
        )
        await self.assertStatus(response, 200)

    @unittest_run_loop
    async def test_all_user_roles(self):
        response = await self.client.get("/ops/all_user_roles/%s" % uuid.uuid1())
        await self.assertStatus(response, 200)
        response_body = await response.json()
        response_body = clean_response_data(response_body)
        validate_response_schema(response_body, schemas.all_user_roles)

    @unittest_run_loop
    async def test_get_domain_roles(self):
        response = await self.client.get("/ops/domain_roles/1")
        await self.assertStatus(response, 200)
        response_body = await response.json()
        response_body = clean_response_data(response_body)
        validate_response_schema(response_body, schemas.domain_roles)

    @unittest_run_loop
    async def test_get_site_and_domain_roles(self):
        response = await self.client.get("/ops/site_and_domain_roles/1")
        await self.assertStatus(response, 200)
        response_body = await response.json()
        response_body = clean_response_data(response_body)
        validate_response_schema(response_body, schemas.site_and_domain_roles)

    @unittest_run_loop
    async def test_get_site_role_labels_aggregated(self):
        response = await self.client.get("/ops/site_role_labels_aggregated/1")
        await self.assertStatus(response, 200)
        response_body = await response.json()
        response_body = clean_response_data(response_body)
        validate_response_schema(response_body, schemas.site_role_labels_aggregated)

    @unittest_run_loop
    async def test_get_user_site_role_labels_aggregated(self):
        response = await self.client.get("/ops/user_site_role_labels_aggregated/%s/1" % uuid.uuid1())
        await self.assertStatus(response, 200)
        response_body = await response.json()
        response_body = clean_response_data(response_body)
        validate_response_schema(response_body, schemas.user_site_role_labels_aggregated)
