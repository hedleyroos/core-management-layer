import asyncio
import json
import logging
from functools import wraps

import time

import access_control.rest
import authentication_service.rest
import user_data_store.rest
from contextlib import contextmanager
from aiohttp import web
from aiohttp.client_exceptions import ClientResponseError, ClientConnectorError, ClientConnectionError

from management_layer.sentry import sentry

logger = logging.getLogger(__name__)


def timeit(log_level=logging.DEBUG):
    def wrap(f):
        @wraps(f)
        async def wrapped_f(*args, **kwargs):
            start_time = time.time()
            if asyncio.iscoroutinefunction(f):
                result = await f(*args, **kwargs)
            else:
                result = f(*args, **kwargs)

            total_time = (time.time() - start_time) * 1000
            logger.log(log_level, f"{f.__module__}.{f.__name__} took {total_time:.3f} ms")

            return result

        return wrapped_f

    return wrap


@contextmanager
def client_exception_handler():
    try:
        try:
            yield
        except Exception:
            # All exceptions are logged to Sentry
            sentry.captureException()
            # We re-raise the exception after logging it to Sentry so that the
            # exception handlers below can do their job.
            raise

    except (access_control.rest.ApiException,
            authentication_service.rest.ApiException,
            user_data_store.rest.ApiException) as re:
        # All API client-related exceptions are handled as "Bad Gateway" errors:
        # The server, while acting as a gateway or proxy, received an invalid
        # response from the upstream server it accessed in attempting to fulfill
        # the request.
        raise web.HTTPBadGateway(
            headers={"content-type": "application/json"},
            text=json.dumps({
                "exception_type": "{}.{}".format(re.__module__, re.__class__.__name__),
                "status": re.status,
                "reason": re.reason,
                "body": re.body
            }))
    except ClientConnectorError as cce:
        raise web.HTTPBadGateway(
            headers={"content-type": "application/json"},
            text=json.dumps({
                "exception_type": "{}.{}".format(cce.__module__, cce.__class__.__name__),
                "status": "N/A",
                "reason": str(cce.os_error),
                "body": str(cce)
            }))
    except ClientConnectionError as cce:
        raise web.HTTPBadGateway(
            headers={"content-type": "application/json"},
            text=json.dumps({
                "exception_type": "{}.{}".format(cce.__module__, cce.__class__.__name__),
                "status": "N/A",
                "reason": str(cce),
                "body": str(cce)
            }))
    except ClientResponseError as cre:
        raise web.HTTPBadGateway(
            headers={"content-type": "application/json"},
            text=json.dumps({
                "exception_type": "{}.{}".format(cre.__module__, cre.__class__.__name__),
                "status": cre.code,
                "reason": cre.message,
                "body": str(cre)
            }))

