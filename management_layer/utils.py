from contextlib import contextmanager

from aiohttp import web

import access_control.rest
import authentication_service.rest
import user_data_store.rest


@contextmanager
def client_exception_handler():
    try:
        yield
    except (access_control.rest.ApiException,
            authentication_service.rest.ApiException,
            user_data_store.rest.ApiException) as re:
        # All client-related exceptions are handled as "Bad Gateway" errors:
        # The server, while acting as a gateway or proxy, received an invalid
        # response from the upstream server it accessed in attempting to fulfill
        # the request.
        raise web.HTTPBadGateway(
            text="Exception Type: {}.{}\nStatus: {}\nReason: {}\nBody: {}".format(
                re.__module__, re.__class__.__name__, re.status, re.reason, re.body))