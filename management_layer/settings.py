import logging
import os


CACHE_TIME = 5 * 60

# Authentication middleware related settings
JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
AUDIENCE = os.getenv("JWT_AUDIENCE")

# Warning: Never set this to true on a production system as it
# bypasses token authentication.
INSECURE = os.getenv("INSECURE", "False").lower() == "true"

# The port to listen on
PORT = os.getenv("PORT", 8000)
WITH_UI = os.getenv("WITH_UI", "False").lower() == "true"

# API locations
ACCESS_CONTROL_API = os.getenv("ACCESS_CONTROL_API")
AUTHENTICATION_SERVICE_API = os.getenv("AUTHENTICATION_SERVICE_API")
USER_DATA_STORE_API = os.getenv("USER_DATA_STORE_API")

LOG_LEVEL = logging.DEBUG
