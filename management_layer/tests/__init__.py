import os


orig_environ = dict(os.environ)
orig_environ["ACCESS_CONTROL_API"] = "localhost/"
orig_environ["AUTHENTICATION_SERVICE_API"] = "localhost/"
orig_environ["USER_DATA_STORE_API"] = "localhost/"
os.environ.update(orig_environ)
