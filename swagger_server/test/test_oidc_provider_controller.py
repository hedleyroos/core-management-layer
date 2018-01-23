# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.client import Client  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestOidcProviderController(BaseTestCase):
    """OidcProviderController integration test stubs"""

    def test_client_list(self):
        """Test case for client_list

        
        """
        query_string = [('offset', 1),
                        ('limit', 100),
                        ('client_ids', 56)]
        response = self.client.open(
            '/api/v1/clients/',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_client_read(self):
        """Test case for client_read

        
        """
        response = self.client.open(
            '/api/v1/clients/{client_id}/'.format(client_id='client_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_delete(self):
        """Test case for user_delete

        
        """
        response = self.client.open(
            '/api/v1/users/{user_id}/'.format(user_id='user_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_list(self):
        """Test case for user_list

        
        """
        query_string = [('offset', 1),
                        ('limit', 100),
                        ('email', 'email_example'),
                        ('user_ids', 'user_ids_example')]
        response = self.client.open(
            '/api/v1/users/',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_read(self):
        """Test case for user_read

        
        """
        response = self.client.open(
            '/api/v1/users/{user_id}/'.format(user_id='user_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_update(self):
        """Test case for user_update

        
        """
        data = User()
        response = self.client.open(
            '/api/v1/users/{user_id}/'.format(user_id='user_id_example'),
            method='PUT',
            data=json.dumps(data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
