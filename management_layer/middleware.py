"""
The middleware module contains functionality that is common to most (if not all) requests.
This module contains functions that performs
* authentication and
* publishing of errors to Sentry.

Performing Authentication:
    Authentication is implemented using JSON Web Tokens (JWT). These tokens form part
    of the OpenID Connect specification. We validation of these tokens is performed using
    the PyJWT library. Care should be taken when interpreting JWTs as most of the information
    is in clear-text and can easily be faked.
    1. It is important to check that the token signature is legitimate. Only then can the rest of
    the information in the token be trusted.
    2. Even when the rest of the information can be trusted, we still need to check that the token
    was issues for the correct audience (this application) and by the current issuer (the
    Authentication Service).

    In OIDC there are trusted and untrusted clients:
    * Trusted clients are able to store a secret where it will not be exposed. An example would be
    our Wagtail demo application.
    * Untrusted clients are not able to store a secret. Javascript applications would be an
    example of these.

    Because trusted clients can share a secret with the Authentication Service, the Authentication
    Service can use an HMAC-based algorithm (HS256) to sign the token. For untrusted clients, the
    Authentication Service uses a public/private key pair (RS256). The token is signed using the
    private key and can then be verified by another party using the public key, which is exposed
    by the Authentication Service at a well-known URL for obtaining a JSON Web Token Keyset
    (JWKS)::

        http://core-authentication-service:8000/openid/jwks

        {
            keys: [
                {
                    kty: "RSA",
                    alg: "RS256",
                    use: "sig",
                    kid: "1cc97496f77201c711529bd6d0159cd3",
                    n: "tQ02VatIRGX2ZC0bu31lxNldo57E3bW8sh...",
                    e: "AQAB"
                }
            ]
        }

    The Management Layer is slightly different from other applications which typically only
    supports a single type of token. The Management Layer needs to support both trusted and
    untrusted clients. When a token is received, we can look at the headers to determine the
    algorithm used to sign the token::

        Unverified headers included in the token for an untrusted client.

        {
            'alg': 'RS256',
            'kid': '1cc97496f77201c711529bd6d0159cd3'
        }

        Unverified headers included in the token for a trusted client.

        {
            'alg': 'HS256'
        }

    When the algorithm is "RS256" there will be a corresponding key id (kid) field, which can
    be used to look up the related key parameters (see JWKS above). The public key can be
    constructed from these parameters.
"""
import jwt
import logging
from aiohttp.web import middleware
from aiohttp.web_response import json_response

from management_layer import settings
from management_layer.mappings import Mappings
from management_layer.sentry import sentry

LOGGER = logging.getLogger(__name__)

INVALID_TOKEN_STATUS = 401
MISSING_TOKEN_STATUS = 400

TOKEN_PREFIX = "bearer "
TOKEN_PREFIX_LENGTH = len(TOKEN_PREFIX)


@middleware
async def auth_middleware(request, handler):
    authorization_header = request.headers.get("authorization", None)
    if authorization_header:
        if not authorization_header.lower().startswith(TOKEN_PREFIX):
            return json_response({"message": "Malformed authorization header"},
                                 status=INVALID_TOKEN_STATUS)

        jwt_token = authorization_header[TOKEN_PREFIX_LENGTH:]
        try:
            LOGGER.debug("JWT Token: {}".format(jwt_token.encode("utf-8")))
            unverified_headers = jwt.get_unverified_header(jwt_token)
            algorithm = unverified_headers["alg"]
            if algorithm == "HS256":
                payload = jwt.decode(
                    jwt_token,
                    key=settings.JWT_SECRET,
                    algorithms=[settings.JWT_ALGORITHM],
                    audience=settings.JWT_AUDIENCE,
                    options={
                        "verify_aud": True
                    }
                )
            elif algorithm == "RS256":
                key_id = unverified_headers["kid"]
                key = Mappings.public_key_for(key_id)
                payload = jwt.decode(
                    jwt_token,
                    key=key,
                    algorithms=[algorithm],
                    audience=settings.JWT_AUDIENCE,
                    options={
                        "verify_aud": True
                    }
                )
            else:
                return json_response({"message": "Unsupported token algorithm: {}".format(algorithm)},
                                     status=INVALID_TOKEN_STATUS)

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
    elif request.method == "OPTIONS":
        # HTTP OPTION requests do not need a token
        pass
    else:
        return json_response({"message": "An authentication token is required"},
                             status=MISSING_TOKEN_STATUS)

    return await handler(request)


# Based on https://github.com/underyx/aiohttp-sentry/blob/master/aiohttp_sentry
@middleware
async def sentry_middleware(request, handler):
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
