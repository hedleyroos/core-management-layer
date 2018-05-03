import asyncio
import datetime
import json
import logging
import uuid
from functools import wraps

import time

import access_control.rest
import authentication_service.rest
import user_data_store.rest
from contextlib import contextmanager
from aiohttp import web
from aiohttp.client_exceptions import ClientResponseError, ClientConnectorError, ClientConnectionError

from access_control import UserWithRoles
from authentication_service import User

from management_layer import mappings, transformations
from management_layer.sentry import sentry

logger = logging.getLogger(__name__)

TESTING_USER_ID = "%s" % uuid.uuid1()


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


async def transform_users_with_roles(request, response, **kwargs):
    """
    Transform a UserWithRole list from the access_control to have id, usernames,
    and role labels for the management layer UserWithRoles schema.
    :return: List of users with roles dicts.
    """
    users_with_roles = [obj.to_dict() for obj in response]

    # Get all user_ids to retrieve.
    user_ids = [
        obj["user_id"] for obj in users_with_roles
    ]
    if user_ids:
        # Get all the user names of the user IDs found.
        users = await request.app[
            "authentication_service_api"].user_list(user_ids=user_ids, **kwargs)

        if users:
            transform = transformations.USER
            users = [transform.apply(user.to_dict()) for user in users]
            user_mapping = {
                user["id"]: user["username"] for user in users
            }
            users_with_roles = [
                {
                    "id": user_with_roles["user_id"],
                    "username": user_mapping[user_with_roles["user_id"]],
                    "roles": [
                        mappings.Mappings.role_label_for(role_id)
                        for role_id in user_with_roles["role_ids"]
                    ]
                } for user_with_roles in users_with_roles
            ]
    return users_with_roles


async def return_users_with_roles(*args, **kwargs):
    """
    Some test functions require a list of user_ids and their role_ids, this is what this
    function will return.
    :return: A list of UserWithRoles objects
    """
    return [
        UserWithRoles(
            user_id=TESTING_USER_ID,
            role_ids=[-1]
        )
    ]


async def return_user_ids(*args, **kwargs):
    """
    Some test functions require to obtain a list of users with at least
    an id and username that is what this will do.
    :return: A list of uuid user_ids
    """
    return [
        User(
            id=TESTING_USER_ID,
            username="Jake",
            is_active=True,
            date_joined=datetime.date.today(),
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()
        )
    ]
