from unittest import TestCase
from unittest.mock import patch
from uuid import uuid1

from datetime import datetime

from management_layer.access_control import RoleResourcePermission
from management_layer.permission import utils

# Test dictionaries commonly used by tests
TEST_ROLES = {"role{}".format(i): i for i in range(1, 11)}
TEST_PERMISSIONS = {"permission{}".format(i): i for i in range(1, 11)}
TEST_RESOURCES = {"urn:resource{}".format(i): i for i in range(1, 11)}


class TestRequirePermissionsDecorator(TestCase):
    """
    These tests exercise the functionality provided by the @require_permissions
    decorator.
    """

    def test_name_and_docstring(self):
        """
        The name attribute and docstring of a decorated function should stay
        the same when the decorator is implemented properly.
        """
        @utils.require_permissions(all, [("urn:ge:test:foo", "read")])
        def simple(_user, _site, **_kwargs):
            """This docstring is checked."""
            pass

        self.assertEqual(simple.__name__, "simple")
        self.assertEqual(simple.__doc__, "This docstring is checked.")

    @patch("management_layer.permission.utils.get_user_roles_for_site")
    def test_empty_resource_permissions_lists(self, mocked_function):
        """
        Check the expected behaviour when an empty resource permission list
        is used with the any or all operation.
        We mock a response for the get_user_roles_for_site() function in
        order to test the case where the specified required resource
        permission list is empty.
        """
        # require_permissions(all, []) always succeeds, regardless of which
        # roles the user has.
        @utils.require_permissions(all, [])
        def empty_all(_user, _site):
            return True

        # require_permissions(any, []) always fails, regardless of which roles
        # the user has.
        @utils.require_permissions(any, [])
        def empty_any(_user, _site):
            raise RuntimeError("This should never get executed")

        mocked_function.return_value = ["some_role"]
        valid_uuid = uuid1()

        # Always gets allowed, regardless of the user's roles
        self.assertTrue(empty_all(valid_uuid, valid_uuid))

        # Never gets allowed, regardless of the user's roles
        with self.assertRaises(utils.Forbidden):
            empty_any(valid_uuid, valid_uuid)

    @patch("management_layer.permission.utils.get_user_roles_for_site")
    def test_positional_args(self, mocked_function):
        """
        Check that positional argument lookups of the user and site
        information works.
        We mock a response for the get_user_roles_for_site() function in
        order check that it was called with the appropriate values.
        """
        @utils.require_permissions(all, [], user_field=2, site_field=1)
        def positional_args(_arg1, _site, _user):
            return True

        user = uuid1()
        site = uuid1()

        # Call the test function...
        positional_args("somevalue", site, user)
        # ...and verify that the mocked function was called with the right
        # arguments.
        mocked_function.assert_called_with(user, site, False)

    @patch("management_layer.permission.utils.get_user_roles_for_site")
    def test_keyword_args(self, mocked_function):
        """
        Check that keyword-based lookups of the user and site information works.
        We mock a response for the get_user_roles_for_site() function in
        order check that it was called with the appropriate values.
        """
        @utils.require_permissions(all, [], user_field="user_id",
                                   site_field="site_id")
        def keyword_args(**kwargs):
            return True

        user = uuid1()
        site = uuid1()

        # Call the test function...
        keyword_args(site_id=site, arg=123, user_id=user)
        # ...and verify that the mocked function was called with the right
        # arguments.
        mocked_function.assert_called_with(user, site, False)

    @patch("management_layer.permission.utils.get_user_roles_for_site")
    def test_mixed_args_nocache(self, mocked_function):
        """
        Check that a mix of positional and keyword-based lookups of user and
        site information works.
        We mock a response for the get_user_roles_for_site() function in
        order check that it was called with the appropriate values.
        """
        @utils.require_permissions(all, [], user_field="user_id",
                                   site_field=1, nocache=True)
        def mixed_args(_arg1, _site, **_kwargs):
            return True

        user = uuid1()
        site = uuid1()

        # Call the test function...
        mixed_args(123, site, user_id=user)
        # ...and verify that the mocked function was called with the right
        # arguments.
        mocked_function.assert_called_with(user, site, True)

    @patch("management_layer.permission.utils.get_user_roles_for_site")
    def test_stacked_decorators(self, mocked_function):
        """
        We mock a response for the get_user_roles_for_site() function in
        order to test the case where the specified required resource
        permission list is empty.
        """
        @utils.require_permissions(all, [])
        @utils.require_permissions(any, [])
        def stack(_user, _site):
            raise RuntimeError("This should never get executed")

        @utils.require_permissions(any, [])
        @utils.require_permissions(all, [])
        def reverse_stack(_user, _site):
            raise RuntimeError("This should never get executed")

        mocked_function.return_value = ["some_role"]
        valid_uuid = uuid1()

        with self.assertRaises(utils.Forbidden):
            stack(valid_uuid, valid_uuid)

        with self.assertRaises(utils.Forbidden):
            reverse_stack(valid_uuid, valid_uuid)

    @patch.dict("management_layer.permission.utils.ROLES",
                {"role1": 1}, clear=True)
    @patch.dict("management_layer.permission.utils.PERMISSIONS",
                {"permission1": 1}, clear=True)
    @patch.dict("management_layer.permission.utils.RESOURCES",
                {"resources1": 1}, clear=True)
    @patch("management_layer.permission.utils.get_user_roles_for_site")
    def test_any(self, mocked_function):
        """
        A test of the 'any' operator by mocking roles, resources and
        permissions.
        """
        mocked_function.return_value = []  # A mocked list of role ids
        pass

    @patch.dict("management_layer.permission.utils.ROLES",
                TEST_ROLES, clear=True)
    @patch.dict("management_layer.permission.utils.PERMISSIONS",
                TEST_PERMISSIONS, clear=True)
    @patch.dict("management_layer.permission.utils.RESOURCES",
                TEST_RESOURCES, clear=True)
    @patch("management_layer.permission.utils.get_role_resource_permissions")
    @patch("management_layer.permission.utils.get_user_roles_for_site")
    def test_all(self, mocked_get_user_roles_for_site,
                 mocked_get_role_resource_permissions):
        """
        A test of the 'all' operator by mocking roles, resources and
        permissions.
        """
        def dummy_get_role_resource_permissions(role, resource, _nocache):
            # Return hand-crafted responses for this test.
            responses = {
                ("role1", "urn:resource1"): [1],
                ("role2", "urn:resource2"): [2],
            }
            return responses.get((role, resource), [])

        mocked_get_role_resource_permissions.side_effect = \
            dummy_get_role_resource_permissions

        @utils.require_permissions(all, [("urn:resource1", "permission1")])
        def single_requirement(_user, _site):
            return True

        # The values for the user and site is not important since this test
        # mocks the roles returned.
        user = uuid1()
        site = uuid1()

        # If the user has no roles, then access is denied.
        mocked_get_user_roles_for_site.return_value = []
        with self.assertRaises(utils.Forbidden):
            single_requirement(user, site)

        # If the user has a role without the necessary permission,
        # then access is denied.
        mocked_get_user_roles_for_site.return_value = ["role2"]
        with self.assertRaises(utils.Forbidden):
            single_requirement(user, site)

        # If the user has a role with the necessary permission,
        # then access is allowed.
        mocked_get_user_roles_for_site.return_value = ["role1"]
        self.assertTrue(single_requirement(user, site))

        @utils.require_permissions(all, [("urn:resource1", "permission1"),
                                         ("urn:resource2", "permission2")])
        def multiple_requirements(_user, _site):
            return True

        # If the user has only one of the permissions, then access is
        # denied.
        mocked_get_user_roles_for_site.return_value = ["role1"]
        with self.assertRaises(utils.Forbidden):
            multiple_requirements(user, site)

        # If the user has all the permissions, then access is allowed.
        mocked_get_user_roles_for_site.return_value = ["role1", "role2"]
        self.assertTrue(multiple_requirements(user, site))

    @patch.dict("management_layer.permission.utils.ROLES",
                TEST_ROLES, clear=True)
    @patch.dict("management_layer.permission.utils.PERMISSIONS",
                TEST_PERMISSIONS, clear=True)
    @patch.dict("management_layer.permission.utils.RESOURCES",
                TEST_RESOURCES, clear=True)
    @patch("management_layer.permission.utils.get_role_resource_permissions")
    @patch("management_layer.permission.utils.get_user_roles_for_site")
    def test_any(self, mocked_get_user_roles_for_site,
                 mocked_get_role_resource_permissions):
        """
        A test of the 'any' operator by mocking roles, resources and
        permissions.
        """
        def dummy_get_role_resource_permissions(role, resource, _nocache):
            # Return hand-crafted responses for this test.
            responses = {
                ("role1", "urn:resource1"): [1],
                ("role2", "urn:resource2"): [2],
            }
            return responses.get((role, resource), [])

        mocked_get_role_resource_permissions.side_effect = \
            dummy_get_role_resource_permissions

        @utils.require_permissions(any, [("urn:resource1", "permission1")])
        def single_requirement(_user, _site):
            return True

        # The values for the user and site is not important since this test
        # mocks the roles returned.
        user = uuid1()
        site = uuid1()

        # If the user has no roles, then access is denied.
        mocked_get_user_roles_for_site.return_value = []
        with self.assertRaises(utils.Forbidden):
            single_requirement(user, site)

        # If the user has a role without the necessary permission,
        # then access is denied.
        mocked_get_user_roles_for_site.return_value = ["role2"]
        with self.assertRaises(utils.Forbidden):
            single_requirement(user, site)

        # If the user has a role with the necessary permission,
        # then access is allowed.
        mocked_get_user_roles_for_site.return_value = ["role1"]
        self.assertTrue(single_requirement(user, site))

        @utils.require_permissions(any, [("urn:resource1", "permission1"),
                                         ("urn:resource2", "permission2")])
        def multiple_requirements(_user, _site):
            return True

        # If the user has any one of the permissions, then access is
        # allowed.
        mocked_get_user_roles_for_site.return_value = ["role1"]
        self.assertTrue(multiple_requirements(user, site))

        mocked_get_user_roles_for_site.return_value = ["role2"]
        self.assertTrue(multiple_requirements(user, site))

        mocked_get_user_roles_for_site.return_value = ["role1", "role2"]
        self.assertTrue(multiple_requirements(user, site))

        # If the user has a role without the necessary permission,
        # then access is denied.
        mocked_get_user_roles_for_site.return_value = ["role3"]
        with self.assertRaises(utils.Forbidden):
            single_requirement(user, site)

    @patch.dict("management_layer.permission.utils.ROLES",
                TEST_ROLES, clear=True)
    @patch.dict("management_layer.permission.utils.PERMISSIONS",
                TEST_PERMISSIONS, clear=True)
    @patch.dict("management_layer.permission.utils.RESOURCES",
                TEST_RESOURCES, clear=True)
    @patch("management_layer.permission.utils.get_role_resource_permissions")
    @patch("management_layer.permission.utils.get_user_roles_for_site")
    def test_combo(self, mocked_get_user_roles_for_site,
                   mocked_get_role_resource_permissions):
        """
        A test of the 'any' operator by mocking roles, resources and
        permissions.

        :param mocked_get_user_roles_for_site: Function mocked by @patch
            decorator
        :param mocked_get_role_resource_permissions: Function mocked by @patch
            decorator
        """
        def dummy_get_role_resource_permissions(role, resource, _nocache):
            # Return hand-crafted responses for this test.
            responses = {
                ("role1", "urn:resource1"): [1],
                ("role2", "urn:resource2"): [2],
                ("role3", "urn:resource3"): [3],
            }
            return responses.get((role, resource), [])

        mocked_get_role_resource_permissions.side_effect = \
            dummy_get_role_resource_permissions

        @utils.require_permissions(all, [("urn:resource1", "permission1")])
        @utils.require_permissions(any, [("urn:resource2", "permission2"),
                                         ("urn:resource3", "permission3")])
        def combo_requirement(_user, _site):
            return True

        # The values for the user and site is not important since this test
        # mocks the roles returned.
        user = uuid1()
        site = uuid1()

        # If the user has no roles, then access is denied.
        mocked_get_user_roles_for_site.return_value = []
        with self.assertRaises(utils.Forbidden):
            combo_requirement(user, site)

        # If the user has roles partially fulfilling the required permissions,
        # then access is denied.
        mocked_get_user_roles_for_site.return_value = ["role1"]
        with self.assertRaises(utils.Forbidden):
            combo_requirement(user, site)

        mocked_get_user_roles_for_site.return_value = ["role2"]
        with self.assertRaises(utils.Forbidden):
            combo_requirement(user, site)

        mocked_get_user_roles_for_site.return_value = ["role3"]
        with self.assertRaises(utils.Forbidden):
            combo_requirement(user, site)

        mocked_get_user_roles_for_site.return_value = ["role2", "role3"]
        with self.assertRaises(utils.Forbidden):
            combo_requirement(user, site)

        # If the user has roles with the necessary permissions,
        # then access is allowed.
        mocked_get_user_roles_for_site.return_value = ["role1", "role2"]
        self.assertTrue(combo_requirement(user, site))

        mocked_get_user_roles_for_site.return_value = ["role1", "role3"]
        self.assertTrue(combo_requirement(user, site))


class TestUtils(TestCase):

    @patch.dict("management_layer.permission.utils.ROLES",
                TEST_ROLES, clear=True)
    @patch.dict("management_layer.permission.utils.PERMISSIONS",
                TEST_PERMISSIONS, clear=True)
    @patch.dict("management_layer.permission.utils.RESOURCES",
                TEST_RESOURCES, clear=True)
    @patch("management_layer.access_control.apis.access_control_api"
           ".AccessControlApi.roleresourcepermission_list")
    def test_role_has_permissions(self, mocked_roleresourcepermission_list):
        """
        Test that the "role_has_permissions" function work as intended.
        :param mocked_roleresourcepermission_list: Function mocked by @patch
            decorator
        """
        def dummy_roleresourcepermission_list(role_id, resource_id):
            responses = {
                (1, 1): [
                    RoleResourcePermission(**{
                        "role_id": role_id,
                        "resource_id": resource_id,
                        "permission_id": TEST_PERMISSIONS["permission1"],
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
                utils.role_has_permission("role1", "permission1",
                                          "urn:resource1", nocache)
            )

            self.assertFalse(
                utils.role_has_permission("role1", "permission2",
                                          "urn:resource1", nocache)
            )

            self.assertFalse(
                utils.role_has_permission("role1", "permission1",
                                          "urn:resource2", nocache)
            )

            # Call function using ids
            self.assertTrue(
                utils.role_has_permission(
                    TEST_ROLES["role1"], TEST_PERMISSIONS["permission1"],
                    TEST_RESOURCES["urn:resource1"], nocache)
            )

            self.assertFalse(
                utils.role_has_permission(
                    TEST_ROLES["role1"], TEST_PERMISSIONS["permission2"],
                    TEST_RESOURCES["urn:resource1"], nocache)
            )

            self.assertFalse(
                utils.role_has_permission(
                    TEST_ROLES["role1"], TEST_PERMISSIONS["permission1"],
                    TEST_RESOURCES["urn:resource2"], nocache)
            )

    @patch.dict("management_layer.permission.utils.ROLES",
                TEST_ROLES, clear=True)
    @patch.dict("management_layer.permission.utils.PERMISSIONS",
                TEST_PERMISSIONS, clear=True)
    @patch.dict("management_layer.permission.utils.RESOURCES",
                TEST_RESOURCES, clear=True)
    @patch("management_layer.access_control.apis.access_control_api"
           ".AccessControlApi.roleresourcepermission_list")
    def test_roles_have_permissions(self, mocked_roleresourcepermission_list):
        """
        Test that the "roles_have_permissions" function work as intended.
        :param mocked_roleresourcepermission_list: Function mocked by @patch
            decorator
        """
        def dummy_roleresourcepermission_list(role_id, resource_id):
            responses = {
                (1, 1): [
                    RoleResourcePermission(**{
                        "role_id": role_id,
                        "resource_id": resource_id,
                        "permission_id": TEST_PERMISSIONS["permission1"],
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
                utils.roles_have_permissions(
                    ["role1", "role2"], all,
                    [("urn:resource1", "permission1")],
                    nocache
                )
            )

            self.assertFalse(
                utils.roles_have_permissions(
                    ["role1", "role2"], all,
                    [("urn:resource1", "permission2")],
                    nocache
                )
            )

            self.assertFalse(
                utils.roles_have_permissions(
                    ["role1", "role2"], all,
                    [("urn:resource2", "permission1")],
                    nocache
                )
            )

            # Call function using ids
            self.assertTrue(
                utils.roles_have_permissions(
                    [TEST_ROLES["role1"], TEST_ROLES["role2"]], all,
                    [(TEST_RESOURCES["urn:resource1"],
                      TEST_PERMISSIONS["permission1"])],
                    nocache
                )
            )

            self.assertFalse(
                utils.roles_have_permissions(
                    [TEST_ROLES["role1"], TEST_ROLES["role2"]], all,
                    [(TEST_RESOURCES["urn:resource1"],
                      TEST_PERMISSIONS["permission2"])],
                    nocache
                )
            )

            self.assertFalse(
                utils.roles_have_permissions(
                    [TEST_ROLES["role1"], TEST_ROLES["role2"]], all,
                    [(TEST_RESOURCES["urn:resource2"],
                      TEST_PERMISSIONS["permission1"])],
                    nocache
                )
            )

        # TODO: Add tests for 'any' operator
