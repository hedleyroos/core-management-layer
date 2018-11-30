from unittest import TestCase
from unittest.mock import Mock, patch

from aiohttp import web
from aiohttp.client_exceptions import ClientResponseError, ClientConnectorError, \
    ClientConnectionError
from aiohttp.test_utils import unittest_run_loop, make_mocked_request, AioHTTPTestCase
from parameterized import parameterized

from management_layer.exceptions import JSONBadGateway
from management_layer.utils import client_exception_handler, return_users, user_with_email_exists
import access_control.rest
import authentication_service.rest
import user_data_store.rest


class ConnectionKey():
    def __init__(self, host, port, ssl):
        self.host = host
        self.port = port
        self.ssl = ssl


class TestClientExceptionHandler(TestCase):

    def test_catch_api_client_errors(self):
        with self.assertRaises(JSONBadGateway):
            with client_exception_handler():
                raise access_control.rest.ApiException

        with self.assertRaises(JSONBadGateway):
            with client_exception_handler():
                raise authentication_service.rest.ApiException

        with self.assertRaises(JSONBadGateway):
            with client_exception_handler():
                raise user_data_store.rest.ApiException

    def test_connection_errors(self):
        with self.assertRaises(JSONBadGateway):
            with client_exception_handler():
                raise ClientConnectionError()

        with self.assertRaises(JSONBadGateway):
            with client_exception_handler():
                connection_key = ConnectionKey(
                    "http://foo.bar", 80, False
                )
                raise ClientConnectorError(
                    connection_key=connection_key,
                    os_error=OSError(1, "one")
                )

        with self.assertRaises(JSONBadGateway):
            with client_exception_handler():
                raise ClientResponseError(
                    request_info="something",
                    history="something"
                )


@patch("authentication_service.api.authentication_api.AuthenticationApi.user_list",
       Mock(side_effect=return_users))
class TestUserWithEmailExists(AioHTTPTestCase):

    async def get_application(self):
        """
        Set up the application used by the tests
        :return:
        """
        app = web.Application(loop=self.loop)

        authentication_service_configuration = authentication_service.configuration.Configuration()
        authentication_service_configuration.host = f"http://localhost:8000/api/v1"
        app["authentication_service_api"] = authentication_service.api.AuthenticationApi(
            api_client=authentication_service.ApiClient(
                configuration=authentication_service_configuration
            )
        )

        async def on_shutdown(the_app):
            await the_app["authentication_service_api"].api_client.rest_client.pool_manager.close()

        app.on_shutdown.append(on_shutdown)
        return app

    @parameterized.expand([
        # (email, expected_result)
        ("jane@example.com", True),
        ("JaNe@eXamplE.com", True),
        ("jane123@example.com", False),
        ("ajane@example.com", False)
    ])
    @unittest_run_loop
    async def test_user_with_email_exists(self, email, expected_result):
        mocked_request = make_mocked_request("GET", "/unused", app=self.app)
        self.assertEqual(
            expected_result,
            await user_with_email_exists(mocked_request, email))
