import os


# Ensure only tests get altered env vars.
from unittest.mock import Mock


def make_coroutine_returning(return_value):
    """
    A utility function used to create coroutines that return a specific value.
    :param return_value: The value that the coroutine should return when awaited.
    :return: A mock coroutine
    """
    async def mock_coroutine(*args, **kwargs):
        return return_value

    return Mock(wraps=mock_coroutine)


if __name__ != "__main__":
    print ("*"*20)
    print ("Test __init__ fired:")
    print (__name__)
    print ("*"*20)

    ACCESS_CONTROL_PORT = 60000
    AUTHENTICATION_SERVICE_PORT = 60001
    USER_DATA_STORE_PORT = 60002
    orig_environ = dict(os.environ)

    # No secrets get updated here. That is still left to each test to sort out.
    orig_environ.update({
        "STUBS_CLASS": "management_layer.integration.Implementation",
        "ACCESS_CONTROL_API": "http://localhost:{}/api/v1".format(ACCESS_CONTROL_PORT),
        "AUTHENTICATION_SERVICE_API": "http://localhost:{}/api/v1".format(AUTHENTICATION_SERVICE_PORT),
        "USER_DATA_STORE_API": "http://localhost:{}/api/v1".format(USER_DATA_STORE_PORT),
        "ACCESS_CONTROL_API_KEY": "test",
        "AUTHENTICATION_SERVICE_API_KEY": "test",
        "USER_DATA_STORE_API_KEY": "test",
        "JWT_AUDIENCE": "test_audience",
        "JWT_SECRET": "test_secret",
        "JWT_ISSUER": "http://localhost:8000/openid",
        "JWT_ALGORITHM": "HS256"
    })
    os.environ.update(orig_environ)
