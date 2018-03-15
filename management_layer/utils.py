import json
from functools import partial

from raven import Client
from raven_aiohttp import QueuedAioHttpTransport

import access_control.rest
import authentication_service.rest
import user_data_store.rest
from contextlib import contextmanager
from aiohttp import web
from aiohttp.client_exceptions import ClientResponseError, ClientConnectorError, ClientConnectionError

SENTRY_DSN = ""
client = Client(
    SENTRY_DSN,
    transport=partial(QueuedAioHttpTransport, workers=5, qsize=1000)
)


@contextmanager
def client_exception_handler():
    try:
        yield
    except (access_control.rest.ApiException,
            authentication_service.rest.ApiException,
            user_data_store.rest.ApiException) as re:
        # All API client-related exceptions are handled as "Bad Gateway" errors:
        # The server, while acting as a gateway or proxy, received an invalid
        # response from the upstream server it accessed in attempting to fulfill
        # the request.
        client.captureException()
        raise web.HTTPBadGateway(
            headers={"content-type": "application/json"},
            text=json.dumps({
                "exception_type": "{}.{}".format(re.__module__, re.__class__.__name__),
                "status": re.status,
                "reason": re.reason,
                "body": re.body
            }))
    except ClientConnectorError as cce:
        client.captureException()
        raise web.HTTPBadGateway(
            headers={"content-type": "application/json"},
            text=json.dumps({
                "exception_type": "{}.{}".format(cce.__module__, cce.__class__.__name__),
                "status": "N/A",
                "reason": str(cce.os_error),
                "body": str(cce)
            }))
    except ClientConnectionError as cce:
        client.captureException()
        raise web.HTTPBadGateway(
            headers={"content-type": "application/json"},
            text=json.dumps({
                "exception_type": "{}.{}".format(cce.__module__, cce.__class__.__name__),
                "status": "N/A",
                "reason": str(cce),
                "body": str(cce)
            }))
    except ClientResponseError as cre:
        client.captureException()
        raise web.HTTPBadGateway(
            headers={"content-type": "application/json"},
            text=json.dumps({
                "exception_type": "{}.{}".format(cre.__module__, cre.__class__.__name__),
                "status": cre.code,
                "reason": cre.message,
                "body": str(cre)
            }))
    except Exception:
        client.captureException()
        raise

