from unittest import TestCase
from unittest.mock import patch
from uuid import uuid1
from management_layer.permission import utils


class TestRequirePermissionsDecorator(TestCase):
    """
    These tests exercise the functionality provided by the @require_permissions
    decorator.
    """
    @classmethod
    def setUpClass(cls):
        pass

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
