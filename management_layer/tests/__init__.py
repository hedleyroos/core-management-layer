import os


# Ensure only tests get altered env vars.
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
    })
    os.environ.update(orig_environ)
