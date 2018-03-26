import logging

from environs import Env

env = Env()


CACHE_TIME = 5 * 60

# Authentication middleware related settings
JWT_SECRET = env.str("JWT_SECRET", None)
JWT_ALGORITHM = env.str("JWT_ALGORITHM", "HS256")
JWT_AUDIENCE = env.str("JWT_AUDIENCE", None)

# Warning: Never set this to true on a production system as it
# bypasses token authentication.
INSECURE = env.bool("INSECURE", False)

# The port to listen on
PORT = env.int("SERVER_PORT", 8000)
WITH_UI = env.bool("WITH_UI", False)

# API locations
ACCESS_CONTROL_API = env.str("ACCESS_CONTROL_API")
AUTHENTICATION_SERVICE_API = env.str("AUTHENTICATION_SERVICE_API")
USER_DATA_STORE_API = env.str("USER_DATA_STORE_API")

# API KEYS
ACCESS_CONTROL_API_KEY = env.str("ACCESS_CONTROL_API_KEY")
AUTHENTICATION_SERVICE_API_KEY = env.str("AUTHENTICATION_SERVICE_API_KEY")
USER_DATA_STORE_API_KEY = env.str("USER_DATA_STORE_API_KEY")

LOG_LEVEL = logging.DEBUG

# Optional Sentry DSN
SENTRY_DSN = env.str("SENTRY_DSN", None)

# Optional Memcache settings
MEMCACHE_HOST = env.str("MEMCACHE_HOST", "localhost")
MEMCACHE_PORT = env.int("MEMCACHE_PORT", 11211)

# Time period between refreshing mapping information.
MAPPING_REFRESH_SLEEP_SECONDS = 10.0
