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
from aiohttp.client_exceptions import ClientResponseError, ClientConnectorError, ClientConnectionError

from access_control import UserWithRoles, Site
from authentication_service import User, Client

from management_layer import mappings, transformations
from management_layer.exceptions import JSONBadGateway
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
        error = json.loads(re.body)["error"] if re.body else None
        raise JSONBadGateway(
            json_data={
                "exception_type": "{}.{}".format(re.__module__, re.__class__.__name__),
                "status": re.status,
                "reason": re.reason,
                "error": error
            })
    except ClientConnectorError as cce:
        raise JSONBadGateway(
            json_data={
                "exception_type": "{}.{}".format(cce.__module__, cce.__class__.__name__),
                "status": "N/A",
                "reason": str(cce.os_error),
                "error": str(cce)
            })
    except ClientConnectionError as cce:
        raise JSONBadGateway(
            json_data={
                "exception_type": "{}.{}".format(cce.__module__, cce.__class__.__name__),
                "status": "N/A",
                "reason": str(cce),
                "error": str(cce)
            })
    except ClientResponseError as cre:
        raise JSONBadGateway(
            json_data={
                "exception_type": "{}.{}".format(cre.__module__, cre.__class__.__name__),
                "status": cre.status,
                "reason": cre.message,
                "error": str(cre)
            })


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
        users = await get_until_complete(
            request, "authentication_service_api", "user_list", **kwargs)

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
                if user_with_roles["user_id"] in user_mapping
            ]
    return users_with_roles


async def get_until_complete(request, api, operation, offset=0, limit=100, **kwargs):
    """
    Perform continuous get calls until all the requested data has been obtained.
    :param request: The current request object.
    :param api: The API to be queried.
    :param operation: The operation to be performed on the given API (with http info).
    :param offset: The current offset of the API call.
    :param limit: The limit of returned results from each call.
    :return: List of data returned.
    """
    with client_exception_handler():
        result = []
        api_call = getattr(request.app[api], operation)
        data = await api_call(offset=offset, limit=limit, **kwargs)
        while data:
            result.extend(data)
            offset += limit
            data = await api_call(offset=offset, limit=limit, **kwargs)
        return result


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


async def return_users(*args, **kwargs):
    """
    Some test functions require to obtain a list of users with at least
    an id and username that is what this will do.
    :return: A list of uuid user_ids
    """
    data = [
        User(
            id=TESTING_USER_ID,
            username="Jake",
            is_active=True,
            date_joined=datetime.date.today(),
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()
        )
    ]
    return data[kwargs["offset"]:]


TEST_SITE = {
    "id": 1,
    "name": "Test Site Name",
    "domain_id": 1,
    "description": "A test site",
    "client_id": 1,
    "is_active": True,
    "created_at": datetime.datetime.now(),
    "updated_at": datetime.datetime.now()
}

TEST_CLIENT = {
    "id": 1,
    "client_id": "test_client",
    "name": "Test Client",
    "contact_email": "",
    "logo": "",
    "require_consent": True,
    "response_type": "",
    "reuse_consent": True
}

TEST_USER = {
    "id": "b001e842-4994-4c74-8db1-bb2caa42298a",
    "username": "username",
    "first_name": "first_name",
    "last_name": "last_name",
    "email": "email@example.com",
    "is_active": True,
    "date_joined": datetime.datetime(2018, 1, 1, 0, 0, 0),
    "last_login": datetime.datetime(2018, 1, 1, 0, 0, 0),
    "birth_date": datetime.datetime(2000, 1, 1, 0, 0, 0),
    "country_code": "za",
    "organisation_id": 1,
    "created_at": datetime.datetime(2018, 1, 1, 0, 0, 0),
    "updated_at": datetime.datetime(2018, 1, 1, 0, 0, 0)
}


async def return_sites(*args, **kwargs):
    """
    Some tests require a test site list to be returned
    """
    return [Site(**TEST_SITE)]


async def return_clients(*args, **kwargs):
    """
    Some tests require a test client list to be returned
    """
    return [Client(**TEST_CLIENT)]


async def return_user(*args, **kwargs):
    """
    Some tests require a test user to be returned
    """
    return User(**TEST_USER)
