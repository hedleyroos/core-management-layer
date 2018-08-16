from copy import copy
from unittest.mock import patch, Mock
from uuid import uuid1

import aioredis
from aiohttp import web
from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop, make_mocked_request

from datetime import datetime

from aiohttp.web import Request
from parameterized import parameterized

from access_control import RoleResourcePermission, AccessControlApi, OperationalApi
from management_layer.constants import TECH_ADMIN_ROLE_LABEL, PORTAL_CONTEXT_HEADER
from management_layer.exceptions import JSONBadRequest, JSONForbidden
from management_layer.mappings import Mappings, return_tech_admin_role_for_testing
from management_layer.permission import utils
from management_layer.permission.decorator import require_permissions, requester_has_role
from management_layer.settings import MANAGEMENT_PORTAL_CLIENT_ID

from management_layer.tests import make_coroutine_returning

TEST_TECH_ADMIN_ROLE_ID = -1
# Test dictionaries commonly used by tests
TEST_ROLES = {i: {"label": f"role{i}"} for i in range(1, 11)}
TEST_ROLE_LABEL_TO_ID_MAP = {v["label"]: k for k, v in TEST_ROLES.items()}
TEST_ROLE_LABEL_TO_ID_MAP[TECH_ADMIN_ROLE_LABEL] = TEST_TECH_ADMIN_ROLE_ID

TEST_PERMISSION_NAME_TO_ID_MAP = {f"permission{i}": i for i in range(1, 11)}

TEST_RESOURCE_URN_TO_ID_MAP = {f"urn:resource{i}": i for i in range(1, 11)}

TEST_SITES = {1: {"name": "Test Site", "client_id": "test_client"}}
TEST_SITE_NAME_TO_ID_MAP = {v["name"]: k for k, v in TEST_SITES.items()}
TEST_TOKEN_CLIENT_ID_TO_SITE_ID_MAP = {v["client_id"]: k for k, v in TEST_SITES.items()}
TEST_TOKEN_CLIENT_ID_TO_SITE_ID_MAP[MANAGEMENT_PORTAL_CLIENT_ID] = 11

TEST_DOMAINS = {1: {"name": "Test Domain"}}
TEST_DOMAIN_NAME_TO_ID_MAP = {v["name"]: k for k, v in TEST_DOMAINS.items()}


@patch.multiple("management_layer.mappings.Mappings",
                _token_client_id_to_site_id_map=TEST_TOKEN_CLIENT_ID_TO_SITE_ID_MAP,
                _role_label_to_id_map=TEST_ROLE_LABEL_TO_ID_MAP,
                _permission_name_to_id_map=TEST_PERMISSION_NAME_TO_ID_MAP,
                _resource_urn_to_id_map=TEST_RESOURCE_URN_TO_ID_MAP)
class TestRequirePermissionsDecorator(AioHTTPTestCase):
    """
    These tests exercise the functionality provided by the @require_permissions
    decorator.
    """
    def setUp(self):
        super().setUp()
        self.user = uuid1()
        self.site_id = 1
        self.client_id = TEST_SITES[self.site_id]["client_id"]
        self.mocked_request = make_mocked_request("GET", "/")
        self.mocked_request["token"] = {
            "sub": str(self.user),
            "aud": self.client_id
        }

    async def get_application(self):
        """
        Set up the application used by the tests
        :return:
        """
        async def hello(request):
            return web.Response(text='Hello, world')

        app = web.Application(loop=self.loop)
        app.router.add_get('/', hello)
        return app

    @patch("management_layer.permission.utils.get_user_roles_for_site")
    @unittest_run_loop
    async def test_target_user_implied_permission(self, mocked_function):
        """
        When a permission decorator specifies a target user field and that field
        contains the user id of the user making the request, then implicit permission
        is granted.
        """
        @require_permissions(any, [], nocache=True, target_user_field=1)
        def example_call_with_user(_request, the_user_id):
            # The caller is also the target user
            return _request["token"]["sub"] == the_user_id

        mocked_function.side_effect = make_coroutine_returning(set())  # No roles

        # Never gets allowed if the user id in the request token does not match
        # the value in the target user field.
        with self.assertRaises(JSONForbidden):
            await example_call_with_user(self.mocked_request, "fake_user_id")

        # Allow the call when the caller is also the target user.
        self.assertTrue(await example_call_with_user(self.mocked_request, str(self.user)))

    @patch("management_layer.permission.utils.get_user_roles_for_site")
    @unittest_run_loop
    async def test_management_portal_allowed_permission(self, mocked_function):
        """
        When a permission decorator specifies that the Management Portal should be
        allowed to make the request, even if the user does not have the permission, the
        permission is granted.
        """
        @require_permissions(any, [], nocache=True, allow_for_management_portal=True)
        def example_call(_request):
            # The caller is also the target user
            return _request["token"]["aud"] == MANAGEMENT_PORTAL_CLIENT_ID

        mocked_function.side_effect = make_coroutine_returning(set())  # No roles

        # This call is not allowed because the request is not made from the Management Portal
        with self.assertRaises(JSONForbidden):
            await example_call(self.mocked_request)

        mocked_request_from_management_portal = copy(self.mocked_request)
        mocked_request_from_management_portal["token"]["aud"] = MANAGEMENT_PORTAL_CLIENT_ID

        # Allow the call when the call is made from the Management Portal
        self.assertTrue(await example_call(mocked_request_from_management_portal))

    @unittest_run_loop
    async def test_name_and_docstring(self):
        """
        The name attribute and docstring of a decorated function should stay
        the same when the decorator is implemented properly.
        """
        @require_permissions(all, [("urn:ge:test:foo", "read")], nocache=True)
        def simple(_request, **_kwargs):
            """This docstring is checked."""
            pass

        self.assertEqual(simple.__name__, "simple")
        self.assertEqual(simple.__doc__, "This docstring is checked.")

    @patch("management_layer.permission.utils.get_user_roles_for_site")
    @unittest_run_loop
    async def test_empty_resource_permissions_lists(self, mocked_function):
        """
        Check the expected behaviour when an empty resource permission list
        is used with the any or all operation.
        We mock a response for the get_user_roles_for_site() function in
        order to test the case where the specified required resource
        permission list is empty.
        """
        # require_permissions(all, []) always succeeds, regardless of which
        # roles the user has.
        @require_permissions(all, [], nocache=True)
        def empty_all(_request):
            return True

        # require_permissions(any, []) always fails, regardless of which roles
        # the user has.
        @require_permissions(any, [], nocache=True)
        def empty_any(_request):
            return "You must be a tech admin"

        mocked_function.side_effect = make_coroutine_returning({0})  # An arbitrary id

        # Always gets allowed, regardless of the user's roles
        self.assertTrue(await empty_all(self.mocked_request))

        # Never gets allowed unless the user has the TECH_ADMIN role
        with self.assertRaises(JSONForbidden):
            await empty_any(self.mocked_request)

        mocked_function.side_effect = make_coroutine_returning(
            {Mappings.role_id_for(TECH_ADMIN_ROLE_LABEL)})
        self.assertEqual(await empty_any(self.mocked_request),
                         "You must be a tech admin")

    @patch("management_layer.permission.utils.get_user_roles_for_site")
    @unittest_run_loop
    async def test_positional_args(self, mocked_function):
        """
        Check that positional argument lookups of the request works.
        We mock a response for the get_user_roles_for_site() function in
        order to check that it was called with the appropriate values.
        """
        @require_permissions(all, [], request_field=1, nocache=True)
        def positional_args(_arg1, _request):
            return True

        mocked_function.side_effect = make_coroutine_returning(set())
        # Call the test function...
        await positional_args("some_value", self.mocked_request)
        # ...and verify that the mocked function was called with the right
        # arguments.
        mocked_function.assert_called_with(self.mocked_request, self.user, self.site_id,
                                           nocache=True)

    @patch("management_layer.permission.utils.get_user_roles_for_site")
    @unittest_run_loop
    async def test_keyword_args(self, mocked_function):
        """
        Check that keyword-based lookups of the user and site information works.
        We mock a response for the get_user_roles_for_site() function in
        order to check that it was called with the appropriate values.
        """
        @require_permissions(all, [], request_field="i_am_a_request", nocache=True)
        def keyword_args(**kwargs):
            return True

        mocked_function.side_effect = make_coroutine_returning(set())
        # Call the test function...
        await keyword_args(arg=123, i_am_a_request=self.mocked_request)
        # ...and verify that the mocked function was called with the right
        # arguments.
        mocked_function.assert_called_with(self.mocked_request, self.user, self.site_id,
                                           nocache=True)

    @patch("management_layer.permission.utils.get_user_roles_for_site")
    @unittest_run_loop
    async def test_stacked_decorators(self, mocked_function):
        """
        We mock a response for the get_user_roles_for_site() function in
        order to test the case where the specified required resource
        permission list is empty.
        """
        @require_permissions(all, [], nocache=True)
        @require_permissions(any, [], nocache=True)
        def stack(_request):
            raise RuntimeError("This should never get executed")

        @require_permissions(any, [], nocache=True)
        @require_permissions(all, [], nocache=True)
        def reverse_stack(_request):
            raise RuntimeError("This should never get executed")

        mocked_function.side_effect = make_coroutine_returning({1000})  # An arbitrary id

        with self.assertRaises(JSONForbidden):
            await stack(self.mocked_request)

        with self.assertRaises(JSONForbidden):
            await reverse_stack(self.mocked_request)

    @patch("management_layer.permission.utils.get_role_resource_permissions")
    @patch("management_layer.permission.utils.get_user_roles_for_site")
    @unittest_run_loop
    async def test_all(self, mocked_get_user_roles_for_site,
                       mocked_get_role_resource_permissions):
        """
        A test of the 'all' operator by mocking roles, resources and
        permissions.
        """
        async def dummy_get_role_resource_permissions(_request, role, resource, nocache=False):
            # Return hand-crafted responses for this test.
            responses = {
                (1, "urn:resource1"): [1],
                (2, "urn:resource2"): [2],
            }
            return responses.get((role, resource), [])

        mocked_get_role_resource_permissions.side_effect = \
            dummy_get_role_resource_permissions

        @require_permissions(all, [("urn:resource1", "permission1")], nocache=True)
        async def single_requirement(_request):
            return True

        # The values for the user and site is not important since this test
        # mocks the roles returned.

        # If the user has no roles, then access is denied.
        mocked_get_user_roles_for_site.side_effect = make_coroutine_returning(set())
        with self.assertRaises(JSONForbidden):
            await single_requirement(self.mocked_request)

        # If the user has a role without the necessary permission,
        # then access is denied.
        mocked_get_user_roles_for_site.side_effect = make_coroutine_returning({2})
        with self.assertRaises(JSONForbidden):
            await single_requirement(self.mocked_request)

        # If the user has a role with the necessary permission,
        # then access is allowed.
        mocked_get_user_roles_for_site.side_effect = make_coroutine_returning({1})
        self.assertTrue(await single_requirement(self.mocked_request))

        @require_permissions(all, [("urn:resource1", "permission1"),
                                   ("urn:resource2", "permission2")], nocache=True)
        def multiple_requirements(_request):
            return True

        # If the user has only one of the permissions, then access is
        # denied.
        mocked_get_user_roles_for_site.side_effect = make_coroutine_returning({1})
        with self.assertRaises(JSONForbidden):
            await multiple_requirements(self.mocked_request)

        # If the user has all the permissions, then access is allowed.
        mocked_get_user_roles_for_site.side_effect = make_coroutine_returning({"role1", "role2"})
        self.assertTrue(await multiple_requirements(self.mocked_request))

    @patch("management_layer.permission.utils.get_role_resource_permissions")
    @patch("management_layer.permission.utils.get_user_roles_for_site")
    @unittest_run_loop
    async def test_any(self, mocked_get_user_roles_for_site,
                       mocked_get_role_resource_permissions):
        """
        A test of the 'any' operator by mocking roles, resources and
        permissions.
        """
        async def dummy_get_role_resource_permissions(_request, role, resource, nocache=False):
            # Return hand-crafted responses for this test.
            responses = {
                (1, "urn:resource1"): [1],
                (2, "urn:resource2"): [2],
            }
            return responses.get((role, resource), [])

        mocked_get_role_resource_permissions.side_effect = \
            dummy_get_role_resource_permissions

        @require_permissions(any, [("urn:resource1", "permission1")], nocache=True)
        def single_requirement(_request):
            return True

        # The values for the user and site is not important since this test
        # mocks the roles returned.

        # If the user has no roles, then access is denied.
        mocked_get_user_roles_for_site.side_effect = make_coroutine_returning(set())
        with self.assertRaises(JSONForbidden):
            await single_requirement(self.mocked_request)

        # If the user has a role without the necessary permission,
        # then access is denied.
        mocked_get_user_roles_for_site.side_effect = make_coroutine_returning({2})
        with self.assertRaises(JSONForbidden):
            await single_requirement(self.mocked_request)

        # If the user has a role with the necessary permission,
        # then access is allowed.
        mocked_get_user_roles_for_site.side_effect = make_coroutine_returning({1})
        self.assertTrue(await single_requirement(self.mocked_request))

        @require_permissions(any, [("urn:resource1", "permission1"),
                                   ("urn:resource2", "permission2")], nocache=True)
        def multiple_requirements(_request):
            return True

        # If the user has any one of the permissions, then access is
        # allowed.
        mocked_get_user_roles_for_site.side_effect = make_coroutine_returning(["role1"])
        self.assertTrue(await multiple_requirements(self.mocked_request))

        mocked_get_user_roles_for_site.side_effect = make_coroutine_returning(["role2"])
        self.assertTrue(await multiple_requirements(self.mocked_request))

        mocked_get_user_roles_for_site.side_effect = make_coroutine_returning(["role1", "role2"])
        self.assertTrue(await multiple_requirements(self.mocked_request))

        # If the user has a role without the necessary permission,
        # then access is denied.
        mocked_get_user_roles_for_site.side_effect = make_coroutine_returning(["role3"])
        with self.assertRaises(JSONForbidden):
            await single_requirement(self.mocked_request)

    @patch("management_layer.permission.utils.get_role_resource_permissions")
    @patch("management_layer.permission.utils.get_user_roles_for_site")
    @unittest_run_loop
    async def test_combo(self, mocked_get_user_roles_for_site,
                         mocked_get_role_resource_permissions):
        """
        A test of the 'any' operator by mocking roles, resources and
        permissions.

        :param mocked_get_user_roles_for_site: Function mocked by @patch
            decorator
        :param mocked_get_role_resource_permissions: Function mocked by @patch
            decorator
        """
        async def dummy_get_role_resource_permissions(_request, role, resource, nocache=False):
            # Return hand-crafted responses for this test.
            responses = {
                (1, "urn:resource1"): [1],
                (2, "urn:resource2"): [2],
                (3, "urn:resource3"): [3],
            }
            return responses.get((role, resource), [])

        mocked_get_role_resource_permissions.side_effect = \
            dummy_get_role_resource_permissions

        @require_permissions(all, [("urn:resource1", "permission1")], nocache=True)
        @require_permissions(any, [("urn:resource2", "permission2"),
                                   ("urn:resource3", "permission3")], nocache=True)
        def combo_requirement(_request):
            return True

        # The values for the user and site is not important since this test
        # mocks the roles returned.

        # If the user has no roles, then access is denied.
        mocked_get_user_roles_for_site.side_effect = make_coroutine_returning(set())
        with self.assertRaises(JSONForbidden):
            await combo_requirement(self.mocked_request)

        # If the user has roles partially fulfilling the required permissions,
        # then access is denied.
        mocked_get_user_roles_for_site.side_effect = make_coroutine_returning({1})
        with self.assertRaises(JSONForbidden):
            await combo_requirement(self.mocked_request)

        mocked_get_user_roles_for_site.side_effect = make_coroutine_returning({2})
        with self.assertRaises(JSONForbidden):
            await combo_requirement(self.mocked_request)

        mocked_get_user_roles_for_site.side_effect = make_coroutine_returning({3})
        with self.assertRaises(JSONForbidden):
            await combo_requirement(self.mocked_request)

        mocked_get_user_roles_for_site.side_effect = make_coroutine_returning({2, 3})
        with self.assertRaises(JSONForbidden):
            await combo_requirement(self.mocked_request)

        # If the user has roles with the necessary permissions,
        # then access is allowed.
        mocked_get_user_roles_for_site.side_effect = make_coroutine_returning({1, 2})
        self.assertTrue(await combo_requirement(self.mocked_request))

        mocked_get_user_roles_for_site.side_effect = make_coroutine_returning({1, 3})
        self.assertTrue(await combo_requirement(self.mocked_request))

    @patch("management_layer.permission.utils.get_user_roles_for_site")
    @patch("management_layer.permission.utils.get_user_roles_for_domain")
    @unittest_run_loop
    async def test_context_header(self, mocked_site_function, mocked_domain_function):
        """
        """
        @require_permissions(all, [("urn:resource1", "permission1")], nocache=True)
        async def somecall(_request):
            return True

        mocked_site_function.side_effect = make_coroutine_returning(set())  # No roles
        mocked_domain_function.side_effect = make_coroutine_returning(set())  # No roles

        # Invalid value
        mocked_request = make_mocked_request("GET", "/", headers={
            PORTAL_CONTEXT_HEADER: "foo"
        })
        mocked_request["token"] = {
            "sub": str(self.user),
            "aud": MANAGEMENT_PORTAL_CLIENT_ID
        }

        with self.assertRaises(JSONBadRequest):
            await somecall(mocked_request)

        # Invalid value
        mocked_request = make_mocked_request("GET", "/", headers={
            PORTAL_CONTEXT_HEADER: "foo:bar"
        })
        mocked_request["token"] = {
            "sub": str(self.user),
            "aud": MANAGEMENT_PORTAL_CLIENT_ID
        }
        with self.assertRaises(JSONBadRequest):
            await somecall(mocked_request)

        # Invalid value
        mocked_request = make_mocked_request("GET", "/", headers={
            PORTAL_CONTEXT_HEADER: "foo:123"
        })
        mocked_request["token"] = {
            "sub": str(self.user),
            "aud": MANAGEMENT_PORTAL_CLIENT_ID
        }
        with self.assertRaises(JSONBadRequest):
            await somecall(mocked_request)

        # Valid header, but Management Portal is not the caller
        mocked_request = make_mocked_request("GET", "/", headers={
            PORTAL_CONTEXT_HEADER: "d:123"
        })
        mocked_request["token"] = {
            "sub": str(self.user),
            "aud": MANAGEMENT_PORTAL_CLIENT_ID + "foo"
        }
        with self.assertRaises(JSONForbidden):
            await somecall(mocked_request)

        # Valid site but not roles
        mocked_request = make_mocked_request("GET", "/", headers={
            PORTAL_CONTEXT_HEADER: "s:123"
        })
        mocked_request["token"] = {
            "sub": str(self.user),
            "aud": MANAGEMENT_PORTAL_CLIENT_ID
        }
        with self.assertRaises(JSONForbidden):
            await somecall(mocked_request)

        # Valid domain, but no roles
        mocked_request = make_mocked_request("GET", "/", headers={
            PORTAL_CONTEXT_HEADER: "d:123"
        })
        mocked_request["token"] = {
            "sub": str(self.user),
            "aud": MANAGEMENT_PORTAL_CLIENT_ID
        }
        with self.assertRaises(JSONForbidden):
            await somecall(mocked_request)

        # Roles will be returned
        mocked_site_function.side_effect = make_coroutine_returning(
            {Mappings.role_id_for(TECH_ADMIN_ROLE_LABEL)}
        )
        mocked_domain_function.side_effect = make_coroutine_returning(
            {Mappings.role_id_for(TECH_ADMIN_ROLE_LABEL)}
        )

        # Valid site
        mocked_request = make_mocked_request("GET", "/", headers={
            PORTAL_CONTEXT_HEADER: "s:123"
        })
        mocked_request["token"] = {
            "sub": str(self.user),
            "aud": MANAGEMENT_PORTAL_CLIENT_ID
        }
        self.assertTrue(await somecall(mocked_request))

        # Valid domain, but no roles
        mocked_request = make_mocked_request("GET", "/", headers={
            PORTAL_CONTEXT_HEADER: "d:123"
        })
        mocked_request["token"] = {
            "sub": str(self.user),
            "aud": MANAGEMENT_PORTAL_CLIENT_ID
        }
        self.assertTrue(await somecall(mocked_request))


@patch.multiple("management_layer.mappings.Mappings",
                _token_client_id_to_site_id_map=TEST_TOKEN_CLIENT_ID_TO_SITE_ID_MAP,
                _sites=TEST_SITES,
                _site_name_to_id_map=TEST_SITE_NAME_TO_ID_MAP,
                _domains=TEST_DOMAINS,
                _domain_name_to_id_map=TEST_DOMAIN_NAME_TO_ID_MAP,
                _roles=TEST_ROLES,
                _role_label_to_id_map=TEST_ROLE_LABEL_TO_ID_MAP,
                _permission_name_to_id_map=TEST_PERMISSION_NAME_TO_ID_MAP,
                _resource_urn_to_id_map=TEST_RESOURCE_URN_TO_ID_MAP)
class TestRequesterHasRoleDecorator(AioHTTPTestCase):
    """
    These tests exercise the functionality provided by the @require_permissions
    decorator.
    """
    def setUp(self):
        super().setUp()
        self.user = uuid1()
        self.site_id = 1
        self.client_id = TEST_SITES[self.site_id]["client_id"]
        self.mocked_request = make_mocked_request("GET", "/")
        self.mocked_request["token"] = {
            "sub": str(self.user),
            "aud": self.client_id
        }

    async def get_application(self):
        """
        Set up the application used by the tests
        :return:
        """
        async def hello(request):
            return web.Response(text='Hello, world')

        app = web.Application(loop=self.loop)
        app.router.add_get('/', hello)
        return app

    @patch("management_layer.permission.utils.get_user_roles_for_domain")
    @unittest_run_loop
    async def test_body_field_with_domain_use_case(self, mocked_get_user_roles_for_domain):
        """
        If a body field is present, it must be a dictionary containing:
        * the target user id (user_id)
        * the role to be assigned (role_id)
        * either the site or domain to which it must be assigned (site_id or role_id)
        """
        @requester_has_role(body_field=1)  # Correct
        def call_with_body(request, body, **kwargs):
            return True

        body = {
            "user_id": self.user.hex,
            "role_id": 1,
            "domain_id": 1
        }

        # Test the case where the requester has no roles for the specified domain.
        mocked_get_user_roles_for_domain.side_effect = make_coroutine_returning(set())

        with self.assertRaises(JSONForbidden):
            await call_with_body(self.mocked_request, body)

        # Test the case where the requester has the role for the specified domain.
        mocked_get_user_roles_for_domain.side_effect = make_coroutine_returning({1})

        self.assertTrue(await call_with_body(self.mocked_request, body))

        # Test the case where the requester has the TECH_ADMIN role
        mocked_get_user_roles_for_domain.side_effect = return_tech_admin_role_for_testing

        self.assertTrue(await call_with_body(self.mocked_request, body))

    @patch("management_layer.permission.utils.get_user_roles_for_site")
    @unittest_run_loop
    async def test_body_field_with_site_use_case(self, mocked_get_user_roles_for_site):
        """
        If a body field is present, it must be a dictionary containing:
        * the target user id (user_id)
        * the role to be assigned (role_id)
        * either the site or domain to which it must be assigned (site_id or role_id)
        """
        @requester_has_role(body_field=1)  # Correct
        def call_with_body(request, body, **kwargs):
            return True

        body = {
            "user_id": self.user.hex,
            "role_id": 1,
            "site_id": 1
        }

        # Test the case where the requester has no roles for the specified domain.
        mocked_get_user_roles_for_site.side_effect = make_coroutine_returning(set())

        with self.assertRaises(JSONForbidden):
            await call_with_body(self.mocked_request, body)

        # Test the case where the requester has the role for the specified domain.
        mocked_get_user_roles_for_site.side_effect = make_coroutine_returning({1})

        self.assertTrue(await call_with_body(self.mocked_request, body))

        # Test the case where the requester has the TECH_ADMIN role
        mocked_get_user_roles_for_site.side_effect = return_tech_admin_role_for_testing

        self.assertTrue(await call_with_body(self.mocked_request, body))

    @parameterized.expand(["target_user_id_field", "target_invitation_id_field"])
    @patch("management_layer.permission.utils.get_user_roles_for_domain")
    @unittest_run_loop
    async def test_no_body_field_with_domain_use_case(
        self, field, mocked_get_user_roles_for_domain
    ):
        kwargs = {
            field: 1,
            "domain_id_field": 2,
            "role_id_field": 3
        }

        @requester_has_role(**kwargs)
        def call_without_body(request, user_or_invitation, domain, role, **kwargs):
            return True

        # Test the case where the requester has no roles for the specified domain.
        mocked_get_user_roles_for_domain.side_effect = make_coroutine_returning(set())

        with self.assertRaises(JSONForbidden):
            await call_without_body(self.mocked_request, self.user.hex, 1, 1)

        # Test the case where the requester has the role for the specified domain.
        mocked_get_user_roles_for_domain.side_effect = make_coroutine_returning({1})

        self.assertTrue(await call_without_body(self.mocked_request, self.user.hex, 1, 1))

        # Test the case where the requester has the TECH_ADMIN role
        mocked_get_user_roles_for_domain.side_effect = return_tech_admin_role_for_testing

        self.assertTrue(await call_without_body(self.mocked_request, self.user.hex, 1, 1))

    @parameterized.expand(["target_user_id_field", "target_invitation_id_field"])
    @patch("management_layer.permission.utils.get_user_roles_for_site")
    @unittest_run_loop
    async def test_no_body_field_with_site_use_case(
        self, field, mocked_get_user_roles_for_site
    ):
        kwargs = {
            field: 1,
            "site_id_field": 2,
            "role_id_field": 3
        }

        @requester_has_role(**kwargs)
        def call_without_body(request, user_or_invitation, site, role, **kwargs):
            return True

        # Test the case where the requester has no roles for the specified domain.
        mocked_get_user_roles_for_site.side_effect = make_coroutine_returning(set())

        with self.assertRaises(JSONForbidden):
            await call_without_body(self.mocked_request, self.user.hex, 1, 1)

        # Test the case where the requester has the role for the specified domain.
        mocked_get_user_roles_for_site.side_effect = make_coroutine_returning({1})

        self.assertTrue(await call_without_body(self.mocked_request, self.user.hex, 1, 1))

        # Test the case where the requester has the TECH_ADMIN role
        mocked_get_user_roles_for_site.side_effect = return_tech_admin_role_for_testing

        self.assertTrue(await call_without_body(self.mocked_request, self.user.hex, 1, 1))

    @patch("management_layer.permission.utils.get_user_roles_for_domain")
    @unittest_run_loop
    async def test_body_field_with_custom_fields_names_and_domain(
            self, mocked_get_user_roles_for_domain):
        """
        If a body field is present, it must be a dictionary containing:
        * the target user id (user_id)
        * the role to be assigned (role_id)
        * either the site or domain to which it must be assigned (site_id or role_id)
        """
        @requester_has_role(request_field=1, body_field=0, target_user_id_field="some_user",
                            domain_id_field="some_domain", role_id_field="some_role")
        def call_with_body(body, request, **kwargs):  # Note that request is not first
            return True

        body = {
            "some_user": self.user.hex,
            "some_role": 1,
            "some_domain": 1
        }

        # Test the case where the requester has no roles for the specified domain.
        mocked_get_user_roles_for_domain.side_effect = make_coroutine_returning(set())

        with self.assertRaises(JSONForbidden):
            await call_with_body(body, self.mocked_request)

        # Test the case where the requester has the role for the specified domain.
        mocked_get_user_roles_for_domain.side_effect = make_coroutine_returning({1})

        self.assertTrue(await call_with_body(body, self.mocked_request))

        # Test the case where the requester has the TECH_ADMIN role
        mocked_get_user_roles_for_domain.side_effect = return_tech_admin_role_for_testing

        self.assertTrue(await call_with_body(body, self.mocked_request))

    @patch("management_layer.permission.utils.get_user_roles_for_site")
    @unittest_run_loop
    async def test_body_field_with_custom_fields_names_and_site(
            self, mocked_get_user_roles_for_site):
        """
        If a body field is present, it must be a dictionary containing:
        * the target user id (user_id)
        * the role to be assigned (role_id)
        * either the site or domain to which it must be assigned (site_id or role_id)
        """
        @requester_has_role(request_field=1, body_field=0, target_user_id_field="some_user",
                            site_id_field="some_site", role_id_field="some_role")
        def call_with_body(body, request, **kwargs):  # Note that request is not first
            return True

        body = {
            "some_user": self.user.hex,
            "some_role": 1,
            "some_site": 1
        }

        # Test the case where the requester has no roles for the specified domain.
        mocked_get_user_roles_for_site.side_effect = make_coroutine_returning(set())

        with self.assertRaises(JSONForbidden):
            await call_with_body(body, self.mocked_request)

        # Test the case where the requester has the role for the specified domain.
        mocked_get_user_roles_for_site.side_effect = make_coroutine_returning({1})

        self.assertTrue(await call_with_body(body, self.mocked_request))

        # Test the case where the requester has the TECH_ADMIN role
        mocked_get_user_roles_for_site.side_effect = return_tech_admin_role_for_testing

        self.assertTrue(await call_with_body(body, self.mocked_request))


@patch.multiple("management_layer.mappings.Mappings",
                _role_label_to_id_map=TEST_ROLE_LABEL_TO_ID_MAP,
                _permission_name_to_id_map=TEST_PERMISSION_NAME_TO_ID_MAP,
                _resource_urn_to_id_map=TEST_RESOURCE_URN_TO_ID_MAP)
class TestUtils(AioHTTPTestCase):

    def setUp(self):
        super().setUp()
        self.dummy_request = Mock(
            spec=Request,
            app=self.app
        )

    async def tearDownAsync(self):
        await super().tearDownAsync()
        self.app["redis"].close()
        await self.app["redis"].wait_closed()
        for backend in ["access_control_api", "operational_api"]:
            await self.app[backend].api_client.rest_client.pool_manager.close()

    async def get_application(self):
        """
        Set up the application used by the tests
        :return:
        """
        async def hello(request):
            return web.Response(text='Hello, world')

        app = web.Application(loop=self.loop)
        app["access_control_api"] = AccessControlApi()
        app["operational_api"] = OperationalApi()
        app["redis"] = await aioredis.create_redis_pool("redis://localhost:6379", loop=self.loop)
        app.router.add_get('/', hello)

        return app

    @patch("access_control.api.access_control_api"
           ".AccessControlApi.roleresourcepermission_list")
    @unittest_run_loop
    async def test_role_has_permissions(self, mocked_roleresourcepermission_list):
        """
        Test that the "role_has_permissions" function work as intended.
        :param mocked_roleresourcepermission_list: Function mocked by @patch
            decorator
        """
        async def dummy_roleresourcepermission_list(role_id, resource_id):
            responses = {
                (1, 1): [
                    RoleResourcePermission(**{
                        "role_id": role_id,
                        "resource_id": resource_id,
                        "permission_id": TEST_PERMISSION_NAME_TO_ID_MAP["permission1"],
                        "created_at": datetime.now(),
                        "updated_at": datetime.now()
                    })
                ]
            }
            return responses.get((role_id, resource_id), [])

        mocked_roleresourcepermission_list.side_effect = \
            dummy_roleresourcepermission_list

        # We test both the cached and non-cached use-cases. It is important
        # that we test with nocache=True first, since this will not read from
        # the cache, but populate it for the next iteration where nocache=False.
        for nocache in [True, False]:
            # Call function using labels
            self.assertTrue(
                await utils.role_has_permission(self.dummy_request,
                                                "role1", "permission1",
                                                "urn:resource1", nocache)
            )

            self.assertFalse(
                await utils.role_has_permission(self.dummy_request,
                                                "role1", "permission2",
                                                "urn:resource1", nocache)
            )

            self.assertFalse(
                await utils.role_has_permission(self.dummy_request,
                                                "role1", "permission1",
                                                "urn:resource2", nocache)
            )

            # Call function using ids
            self.assertTrue(
                await utils.role_has_permission(
                    self.dummy_request,
                    TEST_ROLE_LABEL_TO_ID_MAP["role1"], TEST_PERMISSION_NAME_TO_ID_MAP["permission1"],
                    TEST_RESOURCE_URN_TO_ID_MAP["urn:resource1"], nocache)
            )

            self.assertFalse(
                await utils.role_has_permission(
                    self.dummy_request,
                    TEST_ROLE_LABEL_TO_ID_MAP["role1"], TEST_PERMISSION_NAME_TO_ID_MAP["permission2"],
                    TEST_RESOURCE_URN_TO_ID_MAP["urn:resource1"], nocache)
            )

            self.assertFalse(
                await utils.role_has_permission(
                    self.dummy_request,
                    TEST_ROLE_LABEL_TO_ID_MAP["role1"], TEST_PERMISSION_NAME_TO_ID_MAP["permission1"],
                    TEST_RESOURCE_URN_TO_ID_MAP["urn:resource2"], nocache)
            )

    @patch("access_control.api.access_control_api"
           ".AccessControlApi.roleresourcepermission_list")
    @unittest_run_loop
    async def test_roles_have_permissions(self, mocked_roleresourcepermission_list):
        """
        Test that the "roles_have_permissions" function work as intended.
        :param mocked_roleresourcepermission_list: Function mocked by @patch
            decorator
        """
        async def dummy_roleresourcepermission_list(role_id, resource_id):
            responses = {
                (1, 1): [
                    RoleResourcePermission(**{
                        "role_id": role_id,
                        "resource_id": resource_id,
                        "permission_id": TEST_PERMISSION_NAME_TO_ID_MAP["permission1"],
                        "created_at": datetime.now(),
                        "updated_at": datetime.now()
                    })
                ]
            }
            return responses.get((role_id, resource_id), [])

        mocked_roleresourcepermission_list.side_effect = \
            dummy_roleresourcepermission_list

        # We test both the cached and non-cached use-cases. It is important
        # that we test with nocache=True first, since this will not read from
        # the cache, but populate it for the next iteration where nocache=False.
        # Test using the 'all' operator
        for nocache in [True, False]:
            # Call function using labels
            self.assertTrue(
                await utils.roles_have_permissions(
                    self.dummy_request,
                    {"role1", "role2"}, all,
                    [("urn:resource1", "permission1")],
                    nocache
                )
            )

            self.assertFalse(
                await utils.roles_have_permissions(
                    self.dummy_request,
                    {"role1", "role2"}, all,
                    [("urn:resource1", "permission2")],
                    nocache
                )
            )

            self.assertFalse(
                await utils.roles_have_permissions(
                    self.dummy_request,
                    {"role1", "role2"}, all,
                    [("urn:resource2", "permission1")],
                    nocache
                )
            )

            # Call function using ids
            self.assertTrue(
                await utils.roles_have_permissions(
                    self.dummy_request,
                    {TEST_ROLE_LABEL_TO_ID_MAP["role1"], TEST_ROLE_LABEL_TO_ID_MAP["role2"]}, all,
                    [(TEST_RESOURCE_URN_TO_ID_MAP["urn:resource1"],
                      TEST_PERMISSION_NAME_TO_ID_MAP["permission1"])],
                    nocache
                )
            )

            self.assertFalse(
                await utils.roles_have_permissions(
                    self.dummy_request,
                    {TEST_ROLE_LABEL_TO_ID_MAP["role1"], TEST_ROLE_LABEL_TO_ID_MAP["role2"]}, all,
                    [(TEST_RESOURCE_URN_TO_ID_MAP["urn:resource1"],
                      TEST_PERMISSION_NAME_TO_ID_MAP["permission2"])],
                    nocache
                )
            )

            self.assertFalse(
                await utils.roles_have_permissions(
                    self.dummy_request,
                    {TEST_ROLE_LABEL_TO_ID_MAP["role1"], TEST_ROLE_LABEL_TO_ID_MAP["role2"]}, all,
                    [(TEST_RESOURCE_URN_TO_ID_MAP["urn:resource2"],
                      TEST_PERMISSION_NAME_TO_ID_MAP["permission1"])],
                    nocache
                )
            )

        # Test using the 'any' operator
        for nocache in [True, False]:
            # Call function using labels
            self.assertTrue(
                await utils.roles_have_permissions(
                    self.dummy_request,
                    {"role1", "role2"}, any,
                    [("urn:resource1", "permission1"),
                     ("urn:resource3", "permission3")],
                    nocache
                )
            )

            self.assertFalse(
                await utils.roles_have_permissions(
                    self.dummy_request,
                    {"role1", "role2"}, any,
                    [("urn:resource3", "permission3"),
                     ("urn:resource4", "permission4")],
                    nocache
                )
            )

            self.assertFalse(
                await utils.roles_have_permissions(
                    self.dummy_request,
                    {"role1", "role2"}, any,
                    [("urn:resource2", "permission1")],
                    nocache
                )
            )

            # Call function using ids
            self.assertTrue(
                await utils.roles_have_permissions(
                    self.dummy_request,
                    {TEST_ROLE_LABEL_TO_ID_MAP["role1"], TEST_ROLE_LABEL_TO_ID_MAP["role2"]}, any,
                    [(TEST_RESOURCE_URN_TO_ID_MAP["urn:resource1"],
                      TEST_PERMISSION_NAME_TO_ID_MAP["permission1"]),
                     (TEST_RESOURCE_URN_TO_ID_MAP["urn:resource3"],
                      TEST_PERMISSION_NAME_TO_ID_MAP["permission3"])],
                    nocache
                )
            )

            self.assertFalse(
                await utils.roles_have_permissions(
                    self.dummy_request,
                    {TEST_ROLE_LABEL_TO_ID_MAP["role1"], TEST_ROLE_LABEL_TO_ID_MAP["role2"]}, all,
                    [(TEST_RESOURCE_URN_TO_ID_MAP["urn:resource3"],
                      TEST_PERMISSION_NAME_TO_ID_MAP["permission3"]),
                     (TEST_RESOURCE_URN_TO_ID_MAP["urn:resource4"],
                      TEST_PERMISSION_NAME_TO_ID_MAP["permission4"])],
                    nocache
                )
            )

            self.assertFalse(
                await utils.roles_have_permissions(
                    self.dummy_request,
                    {TEST_ROLE_LABEL_TO_ID_MAP["role1"], TEST_ROLE_LABEL_TO_ID_MAP["role2"]},
                    all,
                    [(TEST_RESOURCE_URN_TO_ID_MAP["urn:resource1"],
                      TEST_PERMISSION_NAME_TO_ID_MAP["permission1"]),
                     (TEST_RESOURCE_URN_TO_ID_MAP["urn:resource3"],
                      TEST_PERMISSION_NAME_TO_ID_MAP["permission3"])],
                    nocache
                )
            )

        # Check that the TECH_ADMIN role grants permission to everything
        # for 'all' and 'any' operator.
        for operator in [all, any]:
            self.assertTrue(
                await utils.roles_have_permissions(
                    self.dummy_request,
                    {Mappings.role_id_for(TECH_ADMIN_ROLE_LABEL)}, operator,
                    [(f"urn:resource{i}", f"permission{i}") for i in range(1, 11)],
                    nocache
                )
            )

    @patch("management_layer.permission.utils.get_role_resource_permissions")
    @patch("management_layer.permission.utils.get_user_roles_for_site")
    @unittest_run_loop
    async def test_user_has_permissions(self, mocked_get_user_roles_for_site,
                                        mocked_get_role_resource_permissions):
        """
        """
        # All users will have only 'role1' on any site
        mocked_get_user_roles_for_site.side_effect = make_coroutine_returning({
            TEST_ROLE_LABEL_TO_ID_MAP["role1"]
        })

        async def dummy_get_role_resource_permissions(_request, role, resource, nocache=False):
            # Return hand-crafted responses for this test.
            role_id = role if type(role) is int else TEST_ROLE_LABEL_TO_ID_MAP[role]
            resource_id = resource if type(resource) is int else \
                TEST_RESOURCE_URN_TO_ID_MAP[resource]
            responses = {
                (1, 1): {TEST_PERMISSION_NAME_TO_ID_MAP["permission1"]},
                (2, 2): {TEST_PERMISSION_NAME_TO_ID_MAP["permission2"]}
            }
            return responses.get((role_id, resource_id), [])

        mocked_get_role_resource_permissions.side_effect = \
            dummy_get_role_resource_permissions

        user = uuid1()
        site = 1

        # Because the user has only role1 assigned and role1 implies only
        # permission1 on resource1, only this one permission check will succeed.
        self.assertTrue(await utils.user_has_permissions(
            self.dummy_request, user, any, [("urn:resource1", "permission1")], site=site
        ))

        self.assertFalse(await utils.user_has_permissions(
            self.dummy_request, user, any, [("urn:resource1", "permission2")], site=site
        ))

        self.assertFalse(await utils.user_has_permissions(
            self.dummy_request, user, any, [("urn:resource2", "permission2")], site=site
        ))

    @unittest_run_loop
    async def test_get_user_roles_for_site_or_domain(self):
        # We just test the validation performed by this function.
        # Other tests cover the lookups.
        user = uuid1()
        site = 1
        domain = 1

        # Either a site or domain must be specified
        with self.assertRaises(RuntimeError):
            await utils.get_user_roles_for_site_or_domain(self.dummy_request, user)

        # Both a site and domain cannot be specified
        with self.assertRaises(RuntimeError):
            await utils.get_user_roles_for_site_or_domain(
                self.dummy_request, user, site=site, domain=domain
            )

    @unittest_run_loop
    async def test_get_role_resource_permissions(self):
        # TODO
        pass

    @unittest_run_loop
    async def test_get_all_user_roles(self):
        # TODO
        pass

    @unittest_run_loop
    async def test_get_user_roles_for_domain(self):
        # TODO
        pass

    @unittest_run_loop
    async def test_get_user_roles_for_site(self):
        # TODO
        pass
