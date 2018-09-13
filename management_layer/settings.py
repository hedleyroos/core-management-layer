from environs import Env

env = Env()


CACHE_TIME = env.int("CACHE_TIME", 5 * 60)

# Authentication middleware related settings
JWT_SECRET = env.str("JWT_SECRET", None)
JWT_ALGORITHM = env.str("JWT_ALGORITHM", "HS256")
JWT_AUDIENCE = env.str("JWT_AUDIENCE", None)
JWT_ISSUER = env.str("JWT_ISSUER", None)

# The port to listen on
PORT = env.int("SERVER_PORT", 8000)
WITH_UI = env.bool("WITH_UI", False)

# API locations
ACCESS_CONTROL_API = env.str("ACCESS_CONTROL_API")
AUTHENTICATION_SERVICE_API = env.str("AUTHENTICATION_SERVICE_API")
USER_DATA_STORE_API = env.str("USER_DATA_STORE_API")

# JWKS location
AUTHENTICATION_SERVICE_JWKS = env.str("AUTHENTICATION_SERVICE_JWKS")

# API KEYS
ACCESS_CONTROL_API_KEY = env.str("ACCESS_CONTROL_API_KEY")
AUTHENTICATION_SERVICE_API_KEY = env.str("AUTHENTICATION_SERVICE_API_KEY")
USER_DATA_STORE_API_KEY = env.str("USER_DATA_STORE_API_KEY")

# Management Portal Client ID (the one used in the token, i.e. client.client_id)
MANAGEMENT_PORTAL_CLIENT_ID = env.str("MANAGEMENT_PORTAL_CLIENT_ID")

LOG_LEVEL = env.str("LOG_LEVEL", "INFO")

# Optional Sentry DSN
SENTRY_DSN = env.str("SENTRY_DSN", None)

# Optional Redis settings
REDIS = env.str("REDIS", "redis://localhost:6379")

# Time period between refreshing mapping information.
MAPPING_REFRESH_SLEEP_SECONDS = env.int("MAPPING_REFRESH_SLEEP_SECONDS", 300)
