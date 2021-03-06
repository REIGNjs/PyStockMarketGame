# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.api_error import ApiError  # noqa: E501
from swagger_server.models.auth_key import AuthKey  # noqa: E501
from swagger_server.models.settings import Settings  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.models.user_prepare_login import UserPrepareLogin  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_create_user(self):
        """Test case for create_user

        Create user
        """
        user_param = User()
        response = self.client.open(
            '/api/user',
            method='POST',
            data=json.dumps(user_param),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_user_settings(self):
        """Test case for create_user_settings

        Create/set settings for logged in user
        """
        settings_param = Settings()
        response = self.client.open(
            '/api/user/settings',
            method='POST',
            data=json.dumps(settings_param),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_user(self):
        """Test case for delete_user

        Delete user
        """
        response = self.client.open(
            '/api/user',
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user(self):
        """Test case for get_user

        Get user from api_key
        """
        response = self.client.open(
            '/api/user',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user_settings(self):
        """Test case for get_user_settings

        Get the settings of the logged in user
        """
        response = self.client.open(
            '/api/user/settings',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_login_user(self):
        """Test case for login_user

        Logs user into the system and returns api key
        """
        user_prepare_login_param = UserPrepareLogin()
        response = self.client.open(
            '/api/user/login',
            method='POST',
            data=json.dumps(user_prepare_login_param),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_logout_user(self):
        """Test case for logout_user

        Logs out current logged in user session
        """
        response = self.client.open(
            '/api/user/logout',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
