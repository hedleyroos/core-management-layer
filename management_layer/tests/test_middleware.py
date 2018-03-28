import time

import jwt
import os
from aiohttp import web
from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
from unittest.mock import patch

from management_layer import middleware


class AuthMiddlewareTest(AioHTTPTestCase):

    async def get_application(self):
        """
        Set up the application used by the tests. For the middleware
        test we only need one end-point.
        :return:
        """
        async def hello(_request):
            return web.Response(text='Hello, world')

        app = web.Application(
            loop=self.loop,
            middlewares=[middleware.auth_middleware]
        )
        app.router.add_get('/', hello)
        return app

    def setUp(self):
        super().setUp()
        now = int(time.time())
        self.id_token_data = {
            "iss": os.environ["JWT_ISSUER"],
            "sub": "bc36b436-1091-11e8-bc0f-0242ac120003",
            "aud": os.environ["JWT_AUDIENCE"],
            "exp": now + 600,  # Expire 5 minutes in the future
            "iat": now,
            "auth_time": now,
            "nonce": "self.code.nonce",
            "at_hash": "QBW0o1FTo_zMzrMc7af94w"
        }

    @unittest_run_loop
    async def test_missing_token(self):
        with patch("management_layer.settings.INSECURE", False):
            response = await self.client.request("GET", "/")
            self.assertEqual(response.status, middleware.MISSING_TOKEN_STATUS)

        with patch("management_layer.settings.INSECURE", True):
            # The token gets faked in insecure mode
            response = await self.client.request("GET", "/")
            self.assertEqual(response.status, 200)

    @unittest_run_loop
    async def test_invalid_token(self):
        response = await self.client.request(
            "GET", "/",
            headers={
                "Authorization": "garbage"
            }
        )
        self.assertEqual(response.status, middleware.INVALID_TOKEN_STATUS)

        response = await self.client.request(
            "GET", "/",
            headers={
                "Authorization": "{}garbage".format(middleware.TOKEN_PREFIX)
            }
        )
        self.assertEqual(response.status, middleware.INVALID_TOKEN_STATUS)

        # Generate a valid token, but fiddle with the expected values
        id_token = jwt.encode(
            payload=self.id_token_data,
            key="somekey",
            algorithm=os.environ["JWT_ALGORITHM"],
        ).decode("utf-8")  # IMPORTANT: Convert token to UTF-8 before embedding in header

        response = await self.client.request(
            "GET", "/",
            headers={
                "Authorization": "bearer {}".format(id_token)
            }
        )
        self.assertEqual(response.status, 401)

        # Fiddle with the audience
        tweaked_data = self.id_token_data.copy()
        tweaked_data["aud"] = "someone_else"
        id_token = jwt.encode(
            payload=tweaked_data,
            key=os.environ["JWT_SECRET"],
            algorithm=os.environ["JWT_ALGORITHM"],
        ).decode("utf-8")  # IMPORTANT: Convert token to UTF-8 before embedding in header

        response = await self.client.request(
            "GET", "/",
            headers={
                "Authorization": "bearer {}".format(id_token)
            }
        )
        self.assertEqual(response.status, 401)

    @unittest_run_loop
    async def test_valid_token(self):
        id_token = jwt.encode(
            payload=self.id_token_data,
            key=os.environ["JWT_SECRET"],
            algorithm=os.environ["JWT_ALGORITHM"],
        ).decode("utf-8")  # IMPORTANT: Convert token to UTF-8 before embedding in header

        response = await self.client.request(
            "GET", "/",
            headers={
                "Authorization": "bearer {}".format(id_token)
            }
        )
        self.assertEqual(response.status, 200)


class SentryMiddlewareTest(AioHTTPTestCase):

    async def get_application(self):
        """
        Set up the application used by the tests. For the middleware
        test we only need one end-point.
        :return:
        """
        async def hello(_request):
            # Always raise an exception
            raise Exception

        app = web.Application(
            loop=self.loop,
            middlewares=[middleware.sentry_middleware]
        )
        app.router.add_get('/', hello)
        return app