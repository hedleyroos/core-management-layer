import jwt
import logging
from aiohttp.web_response import json_response

from management_layer.settings import JWT_SECRET, JWT_ALGORITHM, AUDIENCE, INSECURE

LOGGER = logging.getLogger(__name__)


async def auth_middleware(app, handler):
    async def middleware(request):
        jwt_token = request.headers.get("authorization", None)
        if jwt_token:
            jwt_token = jwt_token.split(" ")[1]  # Strip the "bearer " prefix
            LOGGER.debug("JWT Token: {}".format(jwt_token))
            try:
                payload = jwt.decode(jwt_token, JWT_SECRET,
                                     algorithms=[JWT_ALGORITHM],
                                     audience=AUDIENCE)
                LOGGER.debug("Token payload: {}".format(payload))
            except (jwt.DecodeError, jwt.ExpiredSignatureError):
                return json_response({"message": "Token is invalid"}, status=400)

            request["user_id"] = payload["sub"]
            request["site_id"] = payload["aud"]
            request["token"] = payload
            LOGGER.debug("")
        elif INSECURE:
            request["user_id"] = "test_user"
            request["site_id"] = "test_site"
            request["token"] = {}
            LOGGER.debug("Faking credentials because INSECURE is true.")
        else:
            return json_response({"message": "Token is invalid"}, status=400)

        return await handler(request)
    return middleware
