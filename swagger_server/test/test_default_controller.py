# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_sites_site_id_activate_get(self):
        """Test case for sites_site_id_activate_get

        
        """
        response = self.client.open(
            '/api/v1/sites/{site_id}/activate/'.format(site_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sites_site_id_deactivate_get(self):
        """Test case for sites_site_id_deactivate_get

        
        """
        response = self.client.open(
            '/api/v1/sites/{site_id}/deactivate/'.format(site_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_user_id_activate_get(self):
        """Test case for users_user_id_activate_get

        
        """
        response = self.client.open(
            '/api/v1/users/{user_id}/activate/'.format(user_id='user_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_user_id_deactivate_get(self):
        """Test case for users_user_id_deactivate_get

        
        """
        response = self.client.open(
            '/api/v1/users/{user_id}/deactivate/'.format(user_id='user_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
