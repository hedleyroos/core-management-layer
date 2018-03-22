import jwt
import logging
from aiohttp.web_response import json_response

from management_layer import settings
from management_layer.sentry import sentry

LOGGER = logging.getLogger(__name__)

INVALID_TOKEN_STATUS = 401
MISSING_TOKEN_STATUS = 400

TOKEN_PREFIX = "bearer "
TOKEN_PREFIX_LENGTH = len(TOKEN_PREFIX)


async def auth_middleware(_app, handler):
    async def middleware(request):
        authorization_header = request.headers.get("authorization", None)
        if authorization_header:
            if not authorization_header.lower().startswith(TOKEN_PREFIX):
                return json_response({"message": "Malformed authorization header"},
                                     status=INVALID_TOKEN_STATUS)

            jwt_token = authorization_header[TOKEN_PREFIX_LENGTH:]
            try:
                LOGGER.debug("JWT Token: {}".format(jwt_token.encode("utf-8")))
                LOGGER.debug(jwt.get_unverified_header(jwt_token))
                payload = jwt.decode(
                    jwt_token,
                    key=settings.JWT_SECRET,
                    algorithms=[settings.JWT_ALGORITHM],
                    audience=settings.JWT_AUDIENCE,
                    options={
                        "verify_aud": True
                    }
                )
                LOGGER.debug("Token payload: {}".format(payload))
            except jwt.DecodeError as e:
                return json_response({"message": "Token is invalid: {}".format(e)},
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

            LOGGER.debug("Token payload: {}".format(payload))
            request["token"] = payload
        elif settings.INSECURE:
            request["token"] = {
                "sub": "40b724d6-1d33-11e8-afe3-6f15f0cf1da3",
                "aud": "management_layer_workaround"
            }
            LOGGER.debug("Faking credentials because INSECURE is true.")
        else:
            return json_response({"message": "An authentication token is required"},
                                 status=MISSING_TOKEN_STATUS)

        return await handler(request)
    return middleware


async def sentry_middleware(_app, handler):
    # Based on https://github.com/underyx/aiohttp-sentry/blob/master/aiohttp_sentry
    async def middleware(request):
        try:
            return await handler(request)
        except Exception:
            sentry.captureException(data={
                "request": {
                    "query_string": request.query_string,
                    "cookies": request.headers.get("Cookie", ""),
                    "headers":  dict(request.headers),
                    "url": request.path,
                    "method": request.method,
                    "env": {
                        "REMOTE_ADDR": request.transport.get_extra_info("peername")[0],
                    }
                }
            })
            raise

    return middleware
