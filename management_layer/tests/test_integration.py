import calendar
import json

import aioredis
import jsonschema
import logging
import os
import socket
import subprocess
import time
import uuid

import jwt
from aiohttp import web, ClientSession
from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop, \
    TestClient as Client  # Rename TestClient so that it is not considered a test
from apitools.datagenerator import DataGenerator
from collections import namedtuple
from unittest.mock import patch, Mock

from kinesis_conducer.producer_events.schemas import EventTypes
from parameterized import parameterized

import access_control
import authentication_service
import user_data_store
from management_layer import mappings, transformations
from management_layer.api import schemas
from management_layer.api.urls import add_routes
from management_layer.constants import TECH_ADMIN_ROLE_LABEL
from management_layer.mappings import return_tech_admin_role_for_testing
from management_layer.middleware import auth_middleware, metrics_middleware
from management_layer.utils import return_users_with_roles, return_users, \
    return_sites, TEST_SITE, return_clients, return_user, return_deletedusersite, \
    return_confirmed_deletedusersite

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
    "resource_path", "schema", "create_schema", "update_schema"
])
# A list of resources. Used to parameterise tests.
RESOURCES = {
    "adminnotes": Resource("/1", schemas.admin_note, schemas.admin_note_create, schemas.admin_note_update),
    "credentials": Resource("/1", schemas.credentials, schemas.credentials_create,
                            schemas.credentials_update),
    "deletedusers": Resource("/{}".format(uuid.uuid4()),
                             schemas.deleted_user, schemas.deleted_user_create, schemas.deleted_user_update),
    "deletedusersites": Resource("/{}/{}".format(uuid.uuid4(), 1),
                                 schemas.deleted_user_site, schemas.deleted_user_site_create, schemas.deleted_user_site_update),
    "domains": Resource("/1", schemas.domain, schemas.domain_create, schemas.domain_update),
    "domainroles": Resource("/1/1", schemas.domain_role, schemas.domain_role_create, schemas.domain_role_update),
    "invitations": Resource("/{}".format(uuid.uuid4()),
                            schemas.invitation, schemas.invitation_create, schemas.invitation_update),
    "invitationredirecturls": Resource("/1", schemas.invitation_redirect_url,
                                       schemas.invitation_redirect_url_create,
                                       schemas.invitation_redirect_url_update),
    "invitationdomainroles": Resource("/{}/{}/{}".format(uuid.uuid4(), 1, 1),
                                      schemas.invitation_domain_role, schemas.invitation_domain_role_create, None),
    "invitationsiteroles": Resource("/{}/{}/{}".format(uuid.uuid4(), 1, 1),
                                    schemas.invitation_site_role, schemas.invitation_site_role_create, None),
    "permissions": Resource("/1", schemas.permission, schemas.permission_create, schemas.permission_update),
    "resources": Resource("/1", schemas.resource, schemas.resource_create, schemas.resource_update),
    "roles": Resource("/1", schemas.role, schemas.role_create, schemas.role_update),
    "roleresourcepermissions": Resource("/1/1/1", schemas.role_resource_permission, schemas.role_resource_permission_create, None),
    "sites": Resource("/1", schemas.site, schemas.site_create, schemas.site_update),
    "sitedataschemas": Resource("/1", schemas.site_data_schema, schemas.site_data_schema_create, schemas.site_data_schema_update),
    "siteroles": Resource("/1/1", schemas.site_role, schemas.site_role_create, schemas.site_role_update),
    "userdomainroles": Resource("/{}/{}/{}".format(uuid.uuid4(), 1, 1),
                                schemas.user_domain_role, schemas.user_domain_role_create, None),
    "usersitedata": Resource("/{}/{}".format(uuid.uuid4(), 1),
                             schemas.user_site_data, schemas.user_site_data_create, schemas.user_site_data_update),
    "usersiteroles": Resource("/{}/{}/{}".format(uuid.uuid4(), 1, 1),
                              schemas.user_site_role, schemas.user_site_role_create, None),
    "clients": Resource("/1", schemas.client, None, None),
    "users": Resource("/{}".format(uuid.uuid4()), schemas.user, None, schemas.user_update),
    "countries": Resource("/za", schemas.country, None, None),
    "organisations": Resource("/1", schemas.organisation, schemas.organisation_create, schemas.organisation_update),
    "deletionmethods": Resource("/1", schemas.deletion_method, schemas.deletion_method_create, schemas.deletion_method_update),
}
SKIP_DELETE_TESTS_FOR = ["clients", "countries", "organisations"]


def wait_for_server(ip, port):
    """
    Wait until a server is
    :param ip: The IP address to connect to
    :param port: The port to connect to
    """
    while True:
        try:
            # socket.create_connection() works on MacOS, while socket.socket() with socket.connect()
            # did not.
            s = socket.create_connection((ip, int(port)), timeout=2)
            s.shutdown(2)
            s.close()
            break
        except Exception as e:
            print(e)
            time.sleep(1)


def setUpModule():
    """
    This function is used to launch mocked backend APIs.
    """
    workdir = os.getenv("TRAVIS_BUILD_DIR", ".")
    global _MOCKED_ACCESS_CONTROL_API
    cmd = _PRISM_COMMAND.format(
        workdir, "swagger/access_control.yml", ACCESS_CONTROL_PORT
    )
    LOGGER.info(f"Starting mock server using: {cmd}")
    _MOCKED_ACCESS_CONTROL_API = subprocess.Popen(
        cmd.split(), stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        close_fds=True, shell=False
    )

    global _MOCKED_AUTHENTICATION_SERVICE_API
    cmd = _PRISM_COMMAND.format(
        workdir, "swagger/authentication_service.yml", AUTHENTICATION_SERVICE_PORT
    )
    LOGGER.info(f"Starting mock server using: {cmd}")
    _MOCKED_AUTHENTICATION_SERVICE_API = subprocess.Popen(
        cmd.split(), stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        close_fds=True, shell=False
    )

    global _MOCKED_USER_DATA_STORE_API
    cmd = _PRISM_COMMAND.format(
        workdir, "swagger/user_data_store.yml", USER_DATA_STORE_PORT
    )
    LOGGER.info(f"Starting mock server using: {cmd}")
    _MOCKED_USER_DATA_STORE_API = subprocess.Popen(
        cmd.split(), stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        close_fds=True, shell=False
    )

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
    for field in ["user_id", "creator_id", "invitation_id", "invitor_id",
                  "deleted_user_id", "deleter_id"]:
        if field in data:
            data[field] = str(uuid.uuid1())

    if schema == schemas.deleted_user_create:
        data["id"] = str(uuid.uuid1())

    # Overwrite fields that expect a datetime
    for field in ["consented_at", "last_login", "expires_at", "deleted_at",
                  "deletion_requested_at", "deletion_confirmed_at"]:
        if field in data:
            data[field] = "2000-01-01T00:00:00Z"

    # Overwrite fields that expect a datetime
    for field in ["birth_date"]:
        if field in data:
            data[field] = "2000-01-01"

    if "urn" in data:
        data["urn"] = "urn:ge:test:resource"

    if "url" in data:
        data["url"] = "https://example.com/redirect?foo=bar"

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
            LOGGER.debug(f"Removing field {k} from response because it is None")

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


@patch.multiple("management_layer.mappings.Mappings",
                _token_client_id_to_site_id_map={os.environ["JWT_AUDIENCE"]: 1},
                _roles={-1: {"label": TECH_ADMIN_ROLE_LABEL}},
                _sites={1: transformations.SITE.apply(TEST_SITE)},
                _role_label_to_id_map={TECH_ADMIN_ROLE_LABEL: -1},
                _permission_name_to_id_map={"read": 1},
                _resource_urn_to_id_map={"urn:ge:test:resource": 1,
                                         "urn:ge:test:resource2": 2},
                _account_id_to_credentials_map={
                    "eibahchiefeuchaesheiQuo1leegh9pa": {
                        "account_secret": "OhThufoh0eetheewoochah5sheegh1ye"
                    },
                    "accountwithoutsite": {
                        "account_secret": "somesecret"
                    },
                    "testaccount": {
                        "account_secret": "supersecret"
                    }
                },
                _account_id_to_site_id_map={
                    "eibahchiefeuchaesheiQuo1leegh9pa": 1,
                    "testaccount": 1
                }
                )
@patch("management_layer.permission.utils.get_user_roles_for_site",
       Mock(side_effect=return_tech_admin_role_for_testing))
@patch("management_layer.permission.utils.get_user_roles_for_domain",
       Mock(side_effect=return_tech_admin_role_for_testing))
@patch("access_control.api.operational_api.OperationalApi.get_users_with_roles_for_domain",
       Mock(side_effect=return_users_with_roles))
@patch("access_control.api.operational_api.OperationalApi.get_users_with_roles_for_site",
       Mock(side_effect=return_users_with_roles))
@patch("authentication_service.api.authentication_api.AuthenticationApi.user_list",
       Mock(side_effect=return_users))
@patch("access_control.api.access_control_api.AccessControlApi.site_list",
       Mock(side_effect=return_sites))
@patch("authentication_service.api.authentication_api.AuthenticationApi.client_list",
       Mock(side_effect=return_clients))
@patch("authentication_service.api.authentication_api.AuthenticationApi.user_read",
       Mock(side_effect=return_user))
class IntegrationTest(AioHTTPTestCase):
    """
    Test functionality in integration.py
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user_id = "bc36b436-1091-11e8-bc0f-0242ac120003"

    async def get_client(self, server):
        """
        Return a TestClient instance.
        """
        now = int(time.time())
        id_token_data = {
            "iss": os.environ["JWT_ISSUER"],
            "sub": self.user_id,
            "aud": os.environ["JWT_AUDIENCE"],
            "exp": now + 600,  # Expire 5 minutes in the future
            "iat": now,
            "auth_time": now,
            "nonce": "self.code.nonce",
            "at_hash": "QBW0o1FTo_zMzrMc7af94w"
        }
        id_token = jwt.encode(
            payload=id_token_data,
            key=os.environ["JWT_SECRET"],
            algorithm=os.environ["JWT_ALGORITHM"],
        ).decode("utf-8")
        return Client(
            server, loop=self.loop,
            headers={"Authorization": "Bearer %s" % id_token}
        )

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

        self.assertEqual(status, response.status)

    async def get_application(self):
        """
        Set up the application used by the tests
        :return:
        """
        app = web.Application(loop=self.loop, middlewares=[
            metrics_middleware, auth_middleware
        ])

        user_data_store_configuration = user_data_store.configuration.Configuration()
        user_data_store_configuration.host = f"http://localhost:{USER_DATA_STORE_PORT}/api/v1"
        app["user_data_api"] = user_data_store.api.UserDataApi(
            api_client=user_data_store.ApiClient(
                configuration=user_data_store_configuration
            )
        )

        access_control_configuration = access_control.configuration.Configuration()
        access_control_configuration.host = f"http://localhost:{ACCESS_CONTROL_PORT}/api/v1"
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
        authentication_service_configuration.host = f"http://localhost:{AUTHENTICATION_SERVICE_PORT}/api/v1"
        app["authentication_service_api"] = authentication_service.api.AuthenticationApi(
            api_client=authentication_service.ApiClient(
                configuration=authentication_service_configuration
            )
        )

        app["redis"] = await aioredis.create_redis_pool("redis://localhost:6379", loop=self.loop)

        async def on_startup(the_app):
            the_app["client_session"] = ClientSession()

        async def on_shutdown(the_app):
            await the_app["client_session"].close()
            for backend in [
                "access_control_api",
                "operational_api",
                "authentication_service_api",
                "user_data_api"
            ]:
                await the_app[backend].api_client.rest_client.pool_manager.close()

        app.on_startup.append(on_startup)
        app.on_shutdown.append(on_shutdown)

        add_routes(app, with_ui=False)
        return app

    @parameterized.expand([
        (resource, info) for resource, info in RESOURCES.items()
    ])
    @unittest_run_loop
    async def test_list(self, resource, info):
        # Default call
        response = await self.client.get(f"/{resource}")
        await self.assertStatus(response, 200)
        response_body = await response.json()
        response_body = clean_response_data(response_body)
        validate_response_schema(response_body, {"type": "array", "items": info.schema})
        self.assertIn(_TOTAL_COUNT_HEADER, response.headers)

        # With arguments
        response = await self.client.get(f"/{resource}?offset=1&limit=10")
        await self.assertStatus(response, 200)
        response_body = await response.json()
        response_body = clean_response_data(response_body)
        validate_response_schema(response_body, {"type": "array", "items": info.schema})
        self.assertIn(_TOTAL_COUNT_HEADER, response.headers)

        # With arguments
        response = await self.client.get(f"/{resource}?foo=bar")
        await self.assertStatus(response, 200)
        response_body = await response.json()
        response_body = clean_response_data(response_body)
        validate_response_schema(response_body, {"type": "array", "items": info.schema})
        self.assertIn(_TOTAL_COUNT_HEADER, response.headers)

        # With bad arguments
        response = await self.client.get(f"/{resource}?offset=a")
        await self.assertStatus(response, 400)

        # Quick check that CORS is working
        response = await self.client.request(
            "OPTIONS", f"/{resource}?offset=1&limit=10",
            headers={
                "Origin": "http://foo.bar",
                "Access-Control-Request-Method": "GET"
            }
        )
        await self.assertStatus(response, 200)

        response = await self.client.request(
            "OPTIONS", f"/{resource}?offset=1&limit=10",
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
        response = await self.client.post(f"/{resource}", data=json.dumps(data))
        await self.assertStatus(response, 201)
        response_body = await response.json()
        response_body = clean_response_data(response_body)
        validate_response_schema(response_body, info.schema)

        # Quick check that CORS is working
        response = await self.client.request(
            "OPTIONS", f"/{resource}",
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
            resource, info.resource_path)
        )
        await self.assertStatus(response, 204)

        # Quick check that CORS is working
        response = await self.client.request(
            "OPTIONS", "/{}{}".format(resource, info.resource_path),
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
            resource, info.resource_path)
        )
        await self.assertStatus(response, 200)
        response_body = await response.json()
        response_body = clean_response_data(response_body)
        validate_response_schema(response_body, info.schema)

        # Quick check that CORS is working
        response = await self.client.request(
            "OPTIONS", "/{}{}".format(resource, info.resource_path),
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
            "/{}{}".format(resource, info.resource_path),
            data=json.dumps(data)
        )
        await self.assertStatus(response, 200)
        response_body = await response.json()
        response_body = clean_response_data(response_body)
        validate_response_schema(response_body, info.schema)

        # Quick check that CORS is working
        response = await self.client.request(
            "OPTIONS", "/{}{}".format(resource, info.resource_path),
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
    async def test_get_sites_under_domain(self):
        response = await self.client.get("/ops/get_sites_under_domain/1")
        await self.assertStatus(response, 200)
        response_body = await response.json()
        response_body = clean_response_data(response_body)
        validate_response_schema(response_body, {"type": "array", "items": schemas.site})

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

    @unittest_run_loop
    async def test_get_users_with_roles_for_domain(self):
        response = await self.client.get("/ops/users_with_roles_for_domain/1")
        await self.assertStatus(response, 200)
        response_body = await response.json()
        response_body = clean_response_data(response_body)
        validate_response_schema(response_body[0], schemas.user_with_roles)

    @unittest_run_loop
    async def test_get_users_with_roles_for_domain(self):
        response = await self.client.get("/ops/users_with_roles_for_site/1")
        await self.assertStatus(response, 200)
        response_body = await response.json()
        response_body = clean_response_data(response_body)
        validate_response_schema(response_body[0], schemas.user_with_roles)

    @parameterized.expand(["true", "false"])
    @unittest_run_loop
    async def test_refresh_sites(self, nocache):
        response = await self.client.get("/refresh/sites", params={"nocache": nocache})
        await self.assertStatus(response, 200)

    @parameterized.expand(["true", "false"])
    @unittest_run_loop
    async def test_refresh_roles(self, nocache):
        response = await self.client.get("/refresh/roles", params={"nocache": nocache})
        await self.assertStatus(response, 200)

    @parameterized.expand(["true", "false"])
    @unittest_run_loop
    async def test_refresh_resources(self, nocache):
        response = await self.client.get("/refresh/resources", params={"nocache": nocache})
        await self.assertStatus(response, 200)

    @parameterized.expand(["true", "false"])
    @unittest_run_loop
    async def test_refresh_permissions(self, nocache):
        response = await self.client.get("/refresh/permissions", params={"nocache": nocache})
        await self.assertStatus(response, 200)

    @parameterized.expand(["true", "false"])
    @unittest_run_loop
    async def test_refresh_domains(self, nocache):
        response = await self.client.get("/refresh/domains", params={"nocache": nocache})
        await self.assertStatus(response, 200)

    @parameterized.expand(["true", "false"])
    @unittest_run_loop
    async def test_refresh_keys(self, nocache):
        response = await self.client.get("/refresh/keys", params={"nocache": nocache})
        await self.assertStatus(response, 200)

    @parameterized.expand(["true", "false"])
    @unittest_run_loop
    async def test_refresh_clients(self, nocache):
        response = await self.client.get("/refresh/clients", params={"nocache": nocache})
        await self.assertStatus(response, 200)

    @parameterized.expand(["true", "false"])
    @unittest_run_loop
    async def test_refresh_all(self, nocache):
        response = await self.client.get("/refresh/all", params={"nocache": nocache})
        await self.assertStatus(response, 200)

    @parameterized.expand(["true", "false"])
    @unittest_run_loop
    async def test_user_has_permissions(self, nocache):
        resource_permissions = [
            {
                "resource": "urn:ge:test:resource",
                "permission": "read"
            },
            {
                "resource": "urn:ge:test:resource2",
                "permission": "read"
            },
        ]

        data = {
            "nocache": nocache == "true",
            "operator": "any",
            "resource_permissions": resource_permissions,
            "site_id": 1
        }

        # When the check performed is for the user id that is also the requester (i.e. the
        # holder of the token sent with the request), permission is always allowed to make the
        # request.
        response = await self.client.post(
            f"/ops/user_has_permissions/{self.user_id}",
            data=json.dumps(data)
        )
        await self.assertStatus(response, 200)

        response_body = await response.json()
        validate_response_schema(response_body, schemas.user_permissions_check_response)
        self.assertTrue(response_body["has_permissions"])

        # Quick check that CORS is working
        response = await self.client.request(
            "OPTIONS", f"/ops/user_has_permissions/{self.user_id}",
            headers={
                "Origin": "http://foo.bar",
                "Access-Control-Request-Method": "POST"
            }
        )
        await self.assertStatus(response, 200)

        # Bad requests results in HTTP 400 responses
        data = {
            "nocache": nocache == "true",
            "operator": "unsupported",
            "resource_permissions": resource_permissions,
            "site_id": 1
        }
        response = await self.client.post(
            f"/ops/user_has_permissions/{self.user_id}",
            data=json.dumps(data)
        )
        await self.assertStatus(response, 400)

        data = {
            "nocache": nocache == "true",
            "operator": "any",
            "resource_permissions": resource_permissions,
            # Missing site_id or domain_id
        }
        response = await self.client.post(
            f"/ops/user_has_permissions/{self.user_id}",
            data=json.dumps(data)
        )
        await self.assertStatus(response, 400)

        data = {
            "nocache": nocache == "true",
            "operator": "any",
            "resource_permissions": [
                {
                    "resource": "urn:ge:test:doesnotexist",  # Bad data
                    "permission": "read"
                }
            ],
            "domain_id": 1
        }
        response = await self.client.post(
            f"/ops/user_has_permissions/{self.user_id}",
            data=json.dumps(data)
        )
        await self.assertStatus(response, 400)

    @parameterized.expand(["true", "false"])
    @unittest_run_loop
    async def test_get_user_management_portal_permissions(self, nocache):
        response = await self.client.get(
            "/ops/user_management_portal_permissions/{}".format(self.user_id),
            params={"nocache": nocache})
        await self.assertStatus(response, 200)

        response_body = await response.json()
        validate_response_schema(response_body, {"type": "array", "items": {"type": "string"}})
        # Check that all strings returned have the for "<something>:<somethingelse>"
        for e in response_body:
            resource_urn, permission_name = e.rsplit(":", 1)
            self.assertIn(resource_urn, mappings.Mappings._resource_urn_to_id_map)
            self.assertIn(permission_name, mappings.Mappings._permission_name_to_id_map)

        # Malformed user id
        response = await self.client.get(
            "/ops/user_management_portal_permissions/foobar",
            params={"nocache": nocache})
        await self.assertStatus(response, 400)

    @parameterized.expand(["true", "false"])
    @unittest_run_loop
    async def test_get_user_domain_permissions(self, nocache):
        response = await self.client.get(
            "/ops/user_domain_permissions/{}/{}".format(
                self.user_id, 1),
            params={"nocache": nocache})
        await self.assertStatus(response, 200)

        response_body = await response.json()
        validate_response_schema(response_body, {"type": "array", "items": {"type": "string"}})
        # Check that all strings returned have the for "<something>:<somethingelse>"
        for e in response_body:
            resource_urn, permission_name = e.rsplit(":", 1)
            self.assertIn(resource_urn, mappings.Mappings._resource_urn_to_id_map)
            self.assertIn(permission_name, mappings.Mappings._permission_name_to_id_map)

        # Malformed user id
        response = await self.client.get(
            "/ops/user_domain_permissions/foobar/1",
            params={"nocache": nocache})
        await self.assertStatus(response, 400)

    @parameterized.expand(["true", "false"])
    @unittest_run_loop
    async def test_get_user_site_permissions(self, nocache):
        response = await self.client.get(
            "/ops/user_site_permissions/{}/{}".format(
                self.user_id, 1),
            params={"nocache": nocache})
        await self.assertStatus(response, 200)

        response_body = await response.json()
        validate_response_schema(response_body, {"type": "array", "items": {"type": "string"}})
        # Check that all strings returned have the for "<something>:<somethingelse>"
        for e in response_body:
            resource_urn, permission_name = e.rsplit(":", 1)
            self.assertIn(resource_urn, mappings.Mappings._resource_urn_to_id_map)
            self.assertIn(permission_name, mappings.Mappings._permission_name_to_id_map)

        # Malformed user id
        response = await self.client.get(
            "/ops/user_site_permissions/foobar/1",
            params={"nocache": nocache})
        await self.assertStatus(response, 400)

    @parameterized.expand(["true", "false"])
    @unittest_run_loop
    async def test_get_site_from_client_token_id(self, nocache):
        response = await self.client.get(
            "/ops/get_site_from_client_token_id/{}".format(
                os.environ["JWT_AUDIENCE"]),
            params={"nocache": nocache})
        await self.assertStatus(response, 200)

        response_body = await response.json()
        validate_response_schema(response_body, schemas.site)

        # If the request is for a token id that differs from the
        # one provided in the JWT token's audience, the call is forbidden.
        response = await self.client.get(
            "/ops/get_site_from_client_token_id/some_other_id",
            params={"nocache": nocache})
        await self.assertStatus(response, 403)

    @unittest_run_loop
    async def test_purge_expired_invitations_async(self):
        response = await self.client.get("/invitations/purge/expired")
        await self.assertStatus(response, 200)
        purged_invitations = await response.json()
        validate_response_schema(purged_invitations, schemas.purged_invitations)
        self.assertEqual(purged_invitations["mode"], "asynchronous")

    @unittest_run_loop
    async def test_purge_expired_invitations_sync(self):
        response = await self.client.get("/invitations/purge/expired?synchronous_mode=true")
        await self.assertStatus(response, 200)
        purged_invitations = await response.json()
        validate_response_schema(purged_invitations, schemas.purged_invitations)
        self.assertEqual(purged_invitations["mode"], "synchronous")

    @unittest_run_loop
    async def test_healthcheck(self):
        response = await self.client.get(
            # Overwrite the proper auth header set on the client.
            "/healthcheck", headers={"Authorization": "Unused"}
        )
        self.assertEqual(response.status, 200)
        response_body = await response.json()
        validate_response_schema(response_body, schemas.health_info)

    @unittest_run_loop
    async def test_invitation_send(self):
        invitation_id = uuid.uuid4()
        response = await self.client.get(
            f"/invitations/{invitation_id.hex}/send"
        )
        self.assertEqual(response.status, 200)
        response_body = await response.json()
        self.assertEqual(response_body, None)

    @unittest_run_loop
    async def test_usersitedata_implicit_variants(self):
        # Create usersitedata
        response = await self.client.post(
            "/ops/usersitedata",
            data=json.dumps({"data": {"msg": "test"}})
        )
        await self.assertStatus(response, 201)

        # Read usersitedata
        response = await self.client.get(
            "/ops/usersitedata"
        )
        await self.assertStatus(response, 200)

        response_body = await response.json()
        validate_response_schema(response_body, schemas.user_site_data)

        response_body.pop("user_id")
        response_body.pop("site_id")
        response_body.pop("created_at")
        response_body.pop("updated_at")
        response = await self.client.put(
            "/ops/usersitedata",
            data=json.dumps(response_body)
        )
        await self.assertStatus(response, 200)
        response_body = await response.json()
        validate_response_schema(response_body, schemas.user_site_data)

    @unittest_run_loop
    async def test_user_cannot_delete_himself(self):
        # User deletion
        response = await self.client.delete("/users/{}".format(
            self.user_id  # self.user_id is used in the token as well
        ))
        await self.assertStatus(response, 400)

        # Request user deletion
        data = {
            "user_id": self.user_id,  # self.user_id is used in the token as well
            "reason": "Test"
        }
        response = await self.client.post("/request_user_deletion", data=data)
        await self.assertStatus(response, 400)

    @unittest_run_loop
    async def test_cannot_create_or_update_invitation_for_existing_email(self):
        # Invitation creation with existing email
        invitation_create = {
            "email": "jane@example.com",
            "invitor_id": self.user_id,
            "first_name": "Jane",
            "last_name": "Doe",
            "organisation_id": 1
        }
        expected_response = {"message": "A user with the specified email address already exists."}
        response = await self.client.post("/invitations", json=invitation_create)
        await self.assertStatus(response, 400)
        self.assertEqual(expected_response, await response.json())

        # Invitation update with existing email
        invitation_update = {
            "email": "jane@example.com",
        }
        response = await self.client.put("/invitations/{}".format(uuid.uuid4().hex),
                                         json=invitation_update
                                        )
        await self.assertStatus(response, 400)
        self.assertEqual(expected_response, await response.json())

    @unittest_run_loop
    async def test_confirm_user_data_deletion_expired_request(self):
        params = {
            "account_id": "eibahchiefeuchaesheiQuo1leegh9pa",
            "signature": "definitelynotright",
            "nonce": "",
            "expiry": 0  # This request expired long ago
        }

        # The expiry is in the past and must cause the request to fail
        response = await self.client.get(
            "/ops/confirm_user_data_deletion/{}".format(self.user_id),
            params=params
        )
        await self.assertStatus(response, 401)
        self.assertEqual({"message": "This request has expired."}, await response.json())

    @unittest_run_loop
    async def test_confirm_user_data_deletion_invalid_signature(self):
        params = {
            "account_id": "eibahchiefeuchaesheiQuo1leegh9pa",
            "signature": "definitelynotright",
            "nonce": "",
            "expiry": str(calendar.timegm(time.gmtime()) + 600)  # 5 minutes from now
        }

        response = await self.client.get(
            "/ops/confirm_user_data_deletion/{}".format(self.user_id),
            params=params
        )
        await self.assertStatus(response, 401)
        self.assertEqual({"message": "Invalid signature."}, await response.json())

    @patch("user_data_store.api.user_data_api.UserDataApi.deletedusersite_read",
           Mock(side_effect=return_deletedusersite))
    @patch("user_data_store.api.user_data_api.UserDataApi.deletedusersite_update",
           Mock(side_effect=return_deletedusersite))
    @unittest_run_loop
    async def test_confirm_user_data_deletion_valid_signature_and_nonce_check(self):
        params = {
            "account_id": "eibahchiefeuchaesheiQuo1leegh9pa",
            "signature": "4XANMTcbeAEvTp3eQ5tAmMw-9H2kgdBXstdTN_UM_b8=",
            "nonce": "some_arbitrary_nonce",
            "expiry": 16000000000  # 2477-01-07 06:26:40
        }
        # Ensure nonce is not on Redis
        await self.app["redis"].delete(f"nonce/{params['nonce']}")

        response = await self.client.get(
            "/ops/confirm_user_data_deletion/{}".format(self.user_id),
            params=params
        )
        await self.assertStatus(response, 200)

        # Making the same call again
        response = await self.client.get(
            "/ops/confirm_user_data_deletion/{}".format(self.user_id),
            params=params
        )
        await self.assertStatus(response, 401)
        self.assertEqual({"message": "The specified nonce was already processed."},
                         await response.json())

    @unittest_run_loop
    async def test_confirm_user_data_deletion_account_without_site(self):
        params = {
            "account_id": "accountwithoutsite",
            "signature": "CnI1ePprYMo1LrlOnTTz48Kn_QOMMW636f3z_zbm01I=",
            "nonce": "some_other_arbitrary_nonce",
            "expiry": 16000000000  # 2477-01-07 06:26:40
        }

        response = await self.client.get(
            "/ops/confirm_user_data_deletion/{}".format(self.user_id),
            params=params
        )
        await self.assertStatus(response, 401)
        self.assertEqual({"message": f"Could not find site linked to account "
                                     f"{params['account_id']}."},
                         await response.json())

    @patch("user_data_store.api.user_data_api.UserDataApi.deletedusersite_read",
           Mock(side_effect=return_confirmed_deletedusersite))
    @unittest_run_loop
    async def test_confirm_user_data_deletion_valid_signature_and_nonce_already_confirmed(self):
        params = {
            "account_id": "eibahchiefeuchaesheiQuo1leegh9pa",
            "signature": "4XANMTcbeAEvTp3eQ5tAmMw-9H2kgdBXstdTN_UM_b8=",
            "nonce": "some_arbitrary_nonce",
            "expiry": 16000000000  # 2477-01-07 06:26:40
        }
        # Ensure nonce is not on Redis
        await self.app["redis"].delete(f"nonce/{params['nonce']}")

        with self.assertLogs("management_layer.integration", level=logging.INFO) as logs:
            response = await self.client.get(
                "/ops/confirm_user_data_deletion/{}".format(self.user_id),
                params=params
            )
            await self.assertStatus(response, 200)

        self.assertEqual(logs.output, [
            f"INFO:management_layer.integration:"
            f"Deletion confirmation for user {self.user_id} and site 1 already set."
        ])

    @unittest_run_loop
    async def test_events_create(self):
        # Test unauthorised request
        response = await self.client.post(
            "/events",
            params={
                "account_id": "foobar",
                "event_type": "something",
                "signature": "fake"
            },
            json={
                "foo": "bar"
            }
        )
        await self.assertStatus(response, 401)
        self.assertEqual(await response.json(),
                         {"message": "Invalid signature"})

        # Test authorised request with unknown event type
        response = await self.client.post(
            "/events",
            params={
                "account_id": "testaccount",
                "event_type": "something",
                "signature": "5H6jzDyAbKT-3_yLTK9DC1dym7of3m_jOYGvvMuyToM="
            },
            json={
                "foo": "bar"
            }
        )
        await self.assertStatus(response, 400)
        self.assertEqual(await response.json(),
                         {"message": "Unknown event type"})

        # Test authorised request with valid event type, but one that is not allowed.
        response = await self.client.post(
            "/events",
            params={
                "account_id": "testaccount",
                "event_type": EventTypes.RESOURCE_CRUD,  # Resource CRUD should never be
                                                         # generated by 3rd parties
                "signature": "_4YneHIEVU0jRBXrNwEfkOpnBMIaOc7pqoZpzoFJ91Y="
            },
            json={
                "foo": "bar"
            }
        )
        await self.assertStatus(response, 403)
        self.assertEqual(await response.json(),
                         {"message": "Event type not allowed"})

        # Test authorised request with valid and allowed event type, but a
        # payload that does not match the event type schema.
        response = await self.client.post(
            "/events",
            params={
                "account_id": "testaccount",
                "event_type": EventTypes.USER_LOGIN,  # An allowed event type
                "signature": "rzu2Jw9lhMUd1kKmx8Zh5VDMG7a2W-7p3VJMWKserRc="
            },
            json={
                "foo": "bar"  # Make up an invalid payload
            }
        )
        await self.assertStatus(response, 400)
        self.assertEqual(await response.json(),
                         {"message": "The data does not comply with the schema definition "
                                     "for the specified event type."})

        # Test authorised request with valid and allowed event type,
        # as well as a payload that matches the event type schema.
        with self.assertLogs("management_layer.integration", level=logging.DEBUG) as logs:
            response = await self.client.post(
                "/events",
                params={
                    "account_id": "testaccount",
                    "event_type": EventTypes.USER_LOGIN,
                    "signature": "CDX7n3nHDG7tDjAM2nWg-HjaKsUPkXv5uKRNNnbiHgc="
                },
                json={
                    "user_id": "b964d379-825b-4ad5-98c9-9148aaed532a"  # The expected payload
                }
            )
            await self.assertStatus(response, 201)

        self.assertEqual(logs.output, [
            "DEBUG:management_layer.integration:Event Log: "
            "{'user_id': 'b964d379-825b-4ad5-98c9-9148aaed532a', 'event_type': 'USER_LOGIN', "
            "'site_id': 1}"
        ])