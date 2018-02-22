import json
import logging
import os
import socket
import subprocess
import time
import uuid
from collections import namedtuple

from unittest.mock import patch
from parameterized import parameterized
from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
from aiohttp import web

import access_control
import authentication_service
import user_data_store
from user_data_store import UserDataApi
from management_layer.api import schemas

LOGGER = logging.getLogger(__name__)

# Mocked service ports
ACCESS_CONTROL_PORT = 60000
AUTHENTICATION_SERVICE_PORT = 60001
USER_DATA_STORE_PORT = 60002

with patch.dict(os.environ, {
    "STUBS_CLASS": "management_layer.integration.Implementation",
    "ACCESS_CONTROL_API": "http://localhost:{}/api/v1".format(ACCESS_CONTROL_PORT),
    "AUTHENTICATION_SERVICE_API": "http://localhost:{}/api/v1".format(AUTHENTICATION_SERVICE_PORT),
    "USER_DATA_STORE_API": "http://localhost:{}/api/v1".format(USER_DATA_STORE_PORT),
}):
    # We can only import add_routes once we have mocked the environment
    from management_layer.api.urls import add_routes


_MOCKED_ACCESS_CONTROL_API = None
_MOCKED_AUTHENTICATION_SERVICE_API = None
_MOCKED_USER_DATA_STORE_API = None

_PRISM_COMMAND = "./prism run --validate --mock -s {}/{} -p {}"

Resource = namedtuple("Resource", [
    "num_identifying_parts", "schema", "create_schema", "update_schema"
])
# A list of resources. Used to parameterise tests.
RESOURCES = {
    "adminnotes": Resource(1, schemas.admin_note, schemas.admin_note_create, schemas.admin_note_update),
    "domains": Resource(1, schemas.domain, schemas.domain_create, schemas.domain_update),
    "domainroles": Resource(2, schemas.domain_role, schemas.domain_role_create, schemas.domain_role_update),
    # TODO: Uncomment when these are implemented
    # "invitations": Resource(1),
    # "invitationdomainroles": Resource(3),
    # "invitationsiteroles": Resource(3),
    "permissions": Resource(1, schemas.permission, schemas.permission_create, schemas.permission_update),
    "resources": Resource(1, schemas.resource, schemas.resource_create, schemas.resource_update),
    "roles": Resource(1, schemas.role, schemas.role_create, schemas.role_update),
    "roleresourcepermissions": Resource(3, schemas.role_resource_permission, schemas.role_resource_permission_create, None),
    "sites": Resource(1, schemas.site, schemas.site_create, schemas.site_update),
    "sitedataschemas": Resource(1, schemas.site_data_schema, schemas.site_data_schema_create, schemas.site_data_schema_update),
    "siteroles": Resource(2, schemas.site_role, schemas.site_role_create, schemas.site_role_update),
    "userdomainroles": Resource(3, schemas.user_domain_role, schemas.user_domain_role_create., None),
    "usersitedata": Resource(2, schemas.user_site_data, schemas.user_site_data_create, schemas.user_site_data_update),
    "usersiteroles": Resource(3, schemas.user_site_role, schemas.user_site_role_create, None),
}


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

        authentication_service_configuration = authentication_service.configuration.Configuration()
        authentication_service_configuration.host = "http://localhost:{}/api/v1".format(AUTHENTICATION_SERVICE_PORT)
        app["authentication_service_api"] = authentication_service.api.AuthenticationApi(
            api_client=authentication_service.ApiClient(
                configuration=authentication_service_configuration
            )
        )

        add_routes(app, with_ui=False)
        return app

    @parameterized.expand(RESOURCES.keys())
    @unittest_run_loop
    async def test_list(self, resource):
        # Default call
        reply = await self.client.request("GET", "/{}".format(resource))
        self.assertEqual(reply.status, 200)
        data = await reply.json()
        # Always get a list back
        self.assertIsInstance(data, list)

        # With arguments
        reply = await self.client.request("GET", "/{}?offset=1&limit=10".format(resource))
        self.assertEqual(reply.status, 200)
        data = await reply.json()
        # Always get a list back
        self.assertIsInstance(data, list)

        # With arguments
        reply = await self.client.request("GET", "/{}?user_id=foo".format(resource))
        self.assertEqual(reply.status, 200)
        data = await reply.json()
        # Always get a list back
        self.assertIsInstance(data, list)

        # With bad arguments
        reply = await self.client.request("GET", "/{}?offset=a".format(resource))
        self.assertEqual(reply.status, 400)

    @unittest_run_loop
    async def test_adminnote_create(self):
        data = {
            "user_id": str(uuid.uuid1()),
            "creator_id": str(uuid.uuid1()),
            "note": "A test note"
        }
        # Default call
        request = await self.client.post("/adminnotes", data=json.dumps(data))
        self.assertEqual(request.status, 201)
        admin_note = await request.json()
        # Always get a list back
        self.assertIsInstance(admin_note, dict)
        print(admin_note)

    @parameterized.expand([
        (resource, info) for resource, info in RESOURCES.items()
    ])
    @unittest_run_loop
    async def test_delete(self, resource, info):
        request = await self.client.delete("/{}{}".format(
            resource, "/1" * info.num_identifying_parts)
        )
        if request.status != 204:
            print(resource)
        self.assertEqual(request.status, 204)

    @unittest_run_loop
    async def test_adminnote_read(self):
        request = await self.client.get("/adminnotes/1")
        self.assertEqual(request.status, 200)
        data = await request.json()
        print(data)
        self.assertIn("id", data)
        self.assertIn("creator_id", data)
        self.assertIn("user_id", data)
        self.assertIn("created_at", data)
        self.assertIn("updated_at", data)

    @unittest_run_loop
    async def test_adminnote_update(self):
        data = {
            "note": "An updated note"
        }
        request = await self.client.put("/adminnotes/1", data=json.dumps(data))
        self.assertEqual(request.status, 200)
        admin_note = await request.json()
        print(admin_note)
        self.assertIn("id", admin_note)
        self.assertIn("creator_id", admin_note)
        self.assertIn("user_id", admin_note)
        self.assertIn("created_at", admin_note)
        self.assertIn("updated_at", admin_note)

