import json
import os
import subprocess
import time
import uuid

from unittest.mock import patch
from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
from aiohttp import web

import access_control
import user_data_store
from user_data_store import UserDataApi

ACCESS_CONTROL_PORT = 9000
AUTHENTICATION_SERVICE_PORT = 9001
USER_DATA_STORE_PORT = 9002

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


def setUpModule():
    """
    This function is used to launch mocked backend APIs.
    """
    workdir = os.getenv("TRAVIS_BUILD_DIR", ".")
    global _MOCKED_ACCESS_CONTROL_API
    _MOCKED_ACCESS_CONTROL_API = subprocess.Popen(
        _PRISM_COMMAND.format(
           workdir,  "swagger/access_control.yml", ACCESS_CONTROL_PORT
        ).split()
    )

    global _MOCKED_AUTHENTICATION_SERVICE_API
    _MOCKED_AUTHENTICATION_SERVICE_API = subprocess.Popen(
        _PRISM_COMMAND.format(
            workdir, "swagger/authentication_service.yml", AUTHENTICATION_SERVICE_PORT
        ).split()
    )

    global _MOCKED_USER_DATA_STORE_API
    _MOCKED_USER_DATA_STORE_API = subprocess.Popen(
        _PRISM_COMMAND.format(
            workdir, "swagger/user_data_store.yml", USER_DATA_STORE_PORT
        ).split()
    )
    # Prism needs some time to start up
    time.sleep(8)


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
        user_data_store_configuration.host = "http://localhost:9002/api/v1"
        app["user_data_api"] = UserDataApi(
            api_client=user_data_store.ApiClient(
                configuration=user_data_store_configuration
            )
        )

        access_control_configuration = access_control.configuration.Configuration()
        access_control_configuration.host = "http://localhost:9000/api/v1"
        app["access_control_api"] = access_control.api.AccessControlApi(
            api_client=access_control.ApiClient(
                configuration=access_control_configuration
            )
        )
        # app["user_data_api"] = await utils.get_client(
        #    "../core-access-control/swagger/access_control.yml",
        #    loop=self.loop, host="http://localhost:9002")

        add_routes(app, with_ui=False)
        return app

    @unittest_run_loop
    async def test_adminnote_list(self):
        # Default call
        reply = await self.client.request("GET", "/adminnotes")
        self.assertEqual(reply.status, 200)
        data = await reply.json()
        # Always get a list back
        self.assertIsInstance(data, list)

        # With arguments
        reply = await self.client.request("GET", "/adminnotes?offset=1&limit=10")
        self.assertEqual(reply.status, 200)
        data = await reply.json()
        # Always get a list back
        self.assertIsInstance(data, list)

        # With arguments
        reply = await self.client.request("GET", "/adminnotes?user_id=foo")
        self.assertEqual(reply.status, 200)
        data = await reply.json()
        # Always get a list back
        self.assertIsInstance(data, list)

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

    @unittest_run_loop
    async def test_adminnote_delete(self):
        request = await self.client.delete("/adminnotes/1")
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

    @unittest_run_loop
    async def test_domainrole_list(self):
        # Default call
        reply = await self.client.request("GET", "/domainroles")
        self.assertEqual(reply.status, 200)
        data = await reply.json()
        # Always get a list back
        self.assertIsInstance(data, list)

        # With arguments
        reply = await self.client.request("GET", "/domainroles?offset=1&limit=10")
        self.assertEqual(reply.status, 200)
        data = await reply.json()
        # Always get a list back
        self.assertIsInstance(data, list)

        # With arguments
        reply = await self.client.request("GET", "/domainroles?domain_id=1")
        self.assertEqual(reply.status, 200)
        data = await reply.json()
        # Always get a list back
        self.assertIsInstance(data, list)
