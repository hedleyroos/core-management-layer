import jwt
import logging
from aiohttp.web_response import json_response

from management_layer import settings

LOGGER = logging.getLogger(__name__)

INVALID_TOKEN_STATUS = 401
MISSING_TOKEN_STATUS = 400


async def auth_middleware(app, handler):
    async def middleware(request):
        jwt_token = request.headers.get("authorization", None)
        if jwt_token:
            jwt_token = jwt_token.split(" ")[1]  # Strip the "bearer " prefix
            LOGGER.debug("JWT Token: {}".format(jwt_token))
            LOGGER.debug(jwt.get_unverified_header(jwt_token))
            try:
                payload = jwt.decode(
                    jwt_token,
                    settings.JWT_SECRET,
                    algorithms=[settings.JWT_ALGORITHM],
                    audience=settings.JWT_AUDIENCE
                )
                LOGGER.debug("Token payload: {}".format(payload))
            except jwt.DecodeError:
                return json_response({"message": "Token is invalid"},
                                     status=INVALID_TOKEN_STATUS)
            except jwt.ExpiredSignatureError:
                return json_response({"message": "Token expired"},
                                     status=INVALID_TOKEN_STATUS)
            except jwt.InvalidAudienceError:
                return json_response({"message": "Token audience is invalid"},
                                     status=INVALID_TOKEN_STATUS)
            except jwt.InvalidIssuerError:
                return json_response({"message": "Token issuer is invalid"},
                                     status=INVALID_TOKEN_STATUS)
            except Exception as e:
                return json_response({"message": "Exception: {} {}".format(type(e), str(e))},
                                     status=INVALID_TOKEN_STATUS)

            request["user_id"] = payload["sub"]
            request["client_id"] = payload["aud"]
            request["token"] = payload
            LOGGER.debug("Token payload: {}".format(payload))
        elif settings.INSECURE:
            request["user_id"] = "40b724d6-1d33-11e8-afe3-6f15f0cf1da3"
            request["client_id"] = "management_layer_workaround"
            request["token"] = {}
            LOGGER.debug("Faking credentials because INSECURE is true.")
        else:
            return json_response({"message": "An authentication token is required"},
                                 status=MISSING_TOKEN_STATUS)

        return await handler(request)
    return middleware
