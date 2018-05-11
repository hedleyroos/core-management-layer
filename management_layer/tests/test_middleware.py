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
        # Public/private key pair for RS256 token generation
        self.public_key = b"""-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAymYAhxFTGy+hHkfkpYm3
7A78JF9AvIebzpL5wF4T11h9lXJO09H1tiv+EYDj8xfj/UKZ1OjEQDi7AB7XHF9M
cKaLl0Oms8DiGucbVzIt57Gi6C4000fDZ5nzL/XbxZtgm+eIoTKgTS7A7IjKYb35
S7KKkn1HTLIz1Q/SrDGmlTG6+mJqTyhNjv01eWxKVbLf1J7glLgAnXrYjyz8w5Ga
ALHo6r3kOY2TlqyvLg0ljAWPwObzRXj8xeLuIht7y4g8dKFAOeNSsxojzwEuvTao
HaZTYFh3lvkK0HxqxzOlK1IvWiMcrnK+7uhmSHj+W23n2s92Aoqrx0nTa2zr/RUn
GQIDAQAB
-----END PUBLIC KEY-----
        """
        self.private_key = b"""-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDKZgCHEVMbL6Ee
R+SlibfsDvwkX0C8h5vOkvnAXhPXWH2Vck7T0fW2K/4RgOPzF+P9QpnU6MRAOLsA
HtccX0xwpouXQ6azwOIa5xtXMi3nsaLoLjTTR8NnmfMv9dvFm2Cb54ihMqBNLsDs
iMphvflLsoqSfUdMsjPVD9KsMaaVMbr6YmpPKE2O/TV5bEpVst/UnuCUuACdetiP
LPzDkZoAsejqveQ5jZOWrK8uDSWMBY/A5vNFePzF4u4iG3vLiDx0oUA541KzGiPP
AS69NqgdplNgWHeW+QrQfGrHM6UrUi9aIxyucr7u6GZIeP5bbefaz3YCiqvHSdNr
bOv9FScZAgMBAAECggEAA+NfwTiA+zW4B6fj6ZYytVM4Xs6BpN2KDbbfG2XzRaDK
kNNoVkNjUAOaVuW9+06LL7NW1zM9iepNFVyCT2Y5RrS8W8SN8EgVT+T+rnclUJ0l
/wXcN+7Z/ySC+nnjpfEtMvGIu2gIklMCm8io8qW+o0ijxtqnQv7tZftu1aYCiD0q
ll13kQqodyH5Y4Yz+ZRDp09jPWOSaF7/9YtaaSoCN7TMBjp0nxecvLhKCQZsXy4t
RbniYmBt41EBS+TQfbbHoGTCtENIXShsx21Uw7UqiIzOZPnd90EBWtlVc4yT6A5J
3QFh394ZZceM+ISSqxDzZD9DxvSPEz0gUjTaDN1DsQKBgQDlwT7Zed2dwcdMVikq
cdBhVsE6RhMRmRaKMnwp2kq6O6zYRbRZIDuYLgO2zVk0bBDevf2P6WtBuwBESdO6
pBngmgOdp5oZnLuk9WyX7L6UKHJ+NQ7LBvAawxD/uplpvW6DvabpyAZN4EiU6Snb
xa+EeFI3f++JCg9Ih5lIMcTQFQKBgQDhhMTTOHlZ1UExBHAp5d6VWhH/nfvMqjsq
Qs206mldFSGWOzR6UGB0H3QnFMPsu2Vza5kMR1nthYTNCuNuff9Eo27ZD4suBIS8
SZid7FcWqK3Yd3xRCW6va9SvZNgoL9UL7slJn3b2EELxsFRiTW7+fWZDJGSirbv0
JnxbQs+39QKBgC2sMLZCx49oyhmetyg839O5z0eqTngdGqH2T0ByqJBE9KM5mBRv
l+k0nIBmaelF4kSlOBa3rB6w8eihVHmxzYMcmsNoYfXddl/geenpoikJsVjtazdo
9aocRPDRQ1YF1kZSGTA4Fyi8ATG4+B08Oxv2X0GxKQjw+wDME+iKHDnRAoGAFjVz
BLINEVG1B9S+DwI6N08VcqzmPTOOfAz0IRrsoWQRWLAf7OO5e/YVBDxBRzD1Prab
7d+g9YkumNq3pwv1dZb6tZmYRUHgqII+6154/RxDcovhzEE3i0L9QQCXYO3E91Xe
sMdpebYEQbTxunSRt7I1ver5liOx3Mtld79OoXkCgYEAi1y4hhoJU19G1I62EgXs
n8k0BpJQ0C6BlOPrVmVwC+zV/ZMdxX4Nzm9eYzkaunlQQn49LKxV+dU/PFHfkDMz
Hbsuzyl6p7rni/t0E3MHkuu23rRTS5wpPsQdus0H3U8bZwBbFaA0RNjvxKChDt91
hc58gaeUuJtya8YVGT/bSXU=
-----END PRIVATE KEY-----
        """

    @unittest_run_loop
    async def test_missing_token(self):
        response = await self.client.request("GET", "/")
        self.assertEqual(response.status, middleware.MISSING_TOKEN_STATUS)

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

        id_token = jwt.encode(
            payload=tweaked_data,
            key=self.private_key,
            algorithm="RS256",
            headers={"kid": "a_test_key"}
        ).decode("utf-8")  # IMPORTANT: Convert token to UTF-8 before embedding in header

        with patch.multiple("management_layer.mappings.Mappings",
                            _keys={"a_test_key": {"public_key": self.public_key}}):
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

        id_token = jwt.encode(
            payload=self.id_token_data,
            key=self.private_key,
            algorithm="RS256",
            headers={"kid": "a_test_key"}
        ).decode("utf-8")  # IMPORTANT: Convert token to UTF-8 before embedding in header

        with patch.multiple("management_layer.mappings.Mappings",
                            _keys={"a_test_key": {"public_key": self.public_key}}):
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
