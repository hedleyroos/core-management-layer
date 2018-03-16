from unittest import TestCase
from aiohttp.client_exceptions import ClientResponseError, ClientConnectorError, ClientConnectionError
from aiohttp.web import HTTPBadGateway

from .utils import client_exception_handler
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
        with self.assertRaises(HTTPBadGateway):
            with client_exception_handler():
                raise access_control.rest.ApiException

        with self.assertRaises(HTTPBadGateway):
            with client_exception_handler():
                raise authentication_service.rest.ApiException

        with self.assertRaises(HTTPBadGateway):
            with client_exception_handler():
                raise user_data_store.rest.ApiException

    def test_connection_errors(self):
        with self.assertRaises(HTTPBadGateway):
            with client_exception_handler():
                raise ClientConnectionError()

        with self.assertRaises(HTTPBadGateway):
            with client_exception_handler():
                connection_key = ConnectionKey(
                    "http://foo.bar", 80, False
                )
                raise ClientConnectorError(
                    connection_key=connection_key,
                    os_error=OSError(1, "one")
                )

        with self.assertRaises(HTTPBadGateway):
            with client_exception_handler():
                raise ClientResponseError(
                    request_info="something",
                    history="something"
                )
