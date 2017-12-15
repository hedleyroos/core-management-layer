# coding: utf-8

"""
    Authentication Service API

    This is the API that will be exposed by the Authentication Service.  The Authentication service facilitates user registration and login via web-based flows as defined for the OpenID Connect specification. 

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Client(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'client_id': 'str',
        'redirect_uris': 'list[str]',
        'response_types': 'list[str]',
        'grant_types': 'list[str]',
        'application_type': 'str',
        'contacts': 'list[str]',
        'client_name': 'str',
        'logo_uri': 'str',
        'client_uri': 'str',
        'policy_uri': 'str',
        'tos_uri': 'str',
        'default_max_age': 'int',
        'default_scopes': 'list[str]'
    }

    attribute_map = {
        'client_id': 'client_id',
        'redirect_uris': 'redirect_uris',
        'response_types': 'response_types',
        'grant_types': 'grant_types',
        'application_type': 'application_type',
        'contacts': 'contacts',
        'client_name': 'client_name',
        'logo_uri': 'logo_uri',
        'client_uri': 'client_uri',
        'policy_uri': 'policy_uri',
        'tos_uri': 'tos_uri',
        'default_max_age': 'default_max_age',
        'default_scopes': 'default_scopes'
    }

    def __init__(self, client_id=None, redirect_uris=None, response_types=None, grant_types=None, application_type=None, contacts=None, client_name=None, logo_uri=None, client_uri=None, policy_uri=None, tos_uri=None, default_max_age=None, default_scopes=None):
        """
        Client - a model defined in Swagger
        """

        self._client_id = None
        self._redirect_uris = None
        self._response_types = None
        self._grant_types = None
        self._application_type = None
        self._contacts = None
        self._client_name = None
        self._logo_uri = None
        self._client_uri = None
        self._policy_uri = None
        self._tos_uri = None
        self._default_max_age = None
        self._default_scopes = None

        if client_id is not None:
          self.client_id = client_id
        if redirect_uris is not None:
          self.redirect_uris = redirect_uris
        if response_types is not None:
          self.response_types = response_types
        if grant_types is not None:
          self.grant_types = grant_types
        if application_type is not None:
          self.application_type = application_type
        if contacts is not None:
          self.contacts = contacts
        self.client_name = client_name
        if logo_uri is not None:
          self.logo_uri = logo_uri
        self.client_uri = client_uri
        if policy_uri is not None:
          self.policy_uri = policy_uri
        if tos_uri is not None:
          self.tos_uri = tos_uri
        if default_max_age is not None:
          self.default_max_age = default_max_age
        if default_scopes is not None:
          self.default_scopes = default_scopes

    @property
    def client_id(self):
        """
        Gets the client_id of this Client.

        :return: The client_id of this Client.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this Client.

        :param client_id: The client_id of this Client.
        :type: str
        """

        self._client_id = client_id

    @property
    def redirect_uris(self):
        """
        Gets the redirect_uris of this Client.

        :return: The redirect_uris of this Client.
        :rtype: list[str]
        """
        return self._redirect_uris

    @redirect_uris.setter
    def redirect_uris(self, redirect_uris):
        """
        Sets the redirect_uris of this Client.

        :param redirect_uris: The redirect_uris of this Client.
        :type: list[str]
        """

        self._redirect_uris = redirect_uris

    @property
    def response_types(self):
        """
        Gets the response_types of this Client.

        :return: The response_types of this Client.
        :rtype: list[str]
        """
        return self._response_types

    @response_types.setter
    def response_types(self, response_types):
        """
        Sets the response_types of this Client.

        :param response_types: The response_types of this Client.
        :type: list[str]
        """

        self._response_types = response_types

    @property
    def grant_types(self):
        """
        Gets the grant_types of this Client.

        :return: The grant_types of this Client.
        :rtype: list[str]
        """
        return self._grant_types

    @grant_types.setter
    def grant_types(self, grant_types):
        """
        Sets the grant_types of this Client.

        :param grant_types: The grant_types of this Client.
        :type: list[str]
        """

        self._grant_types = grant_types

    @property
    def application_type(self):
        """
        Gets the application_type of this Client.

        :return: The application_type of this Client.
        :rtype: str
        """
        return self._application_type

    @application_type.setter
    def application_type(self, application_type):
        """
        Sets the application_type of this Client.

        :param application_type: The application_type of this Client.
        :type: str
        """

        self._application_type = application_type

    @property
    def contacts(self):
        """
        Gets the contacts of this Client.

        :return: The contacts of this Client.
        :rtype: list[str]
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        """
        Sets the contacts of this Client.

        :param contacts: The contacts of this Client.
        :type: list[str]
        """

        self._contacts = contacts

    @property
    def client_name(self):
        """
        Gets the client_name of this Client.

        :return: The client_name of this Client.
        :rtype: str
        """
        return self._client_name

    @client_name.setter
    def client_name(self, client_name):
        """
        Sets the client_name of this Client.

        :param client_name: The client_name of this Client.
        :type: str
        """
        if client_name is None:
            raise ValueError("Invalid value for `client_name`, must not be `None`")

        self._client_name = client_name

    @property
    def logo_uri(self):
        """
        Gets the logo_uri of this Client.

        :return: The logo_uri of this Client.
        :rtype: str
        """
        return self._logo_uri

    @logo_uri.setter
    def logo_uri(self, logo_uri):
        """
        Sets the logo_uri of this Client.

        :param logo_uri: The logo_uri of this Client.
        :type: str
        """

        self._logo_uri = logo_uri

    @property
    def client_uri(self):
        """
        Gets the client_uri of this Client.

        :return: The client_uri of this Client.
        :rtype: str
        """
        return self._client_uri

    @client_uri.setter
    def client_uri(self, client_uri):
        """
        Sets the client_uri of this Client.

        :param client_uri: The client_uri of this Client.
        :type: str
        """
        if client_uri is None:
            raise ValueError("Invalid value for `client_uri`, must not be `None`")

        self._client_uri = client_uri

    @property
    def policy_uri(self):
        """
        Gets the policy_uri of this Client.

        :return: The policy_uri of this Client.
        :rtype: str
        """
        return self._policy_uri

    @policy_uri.setter
    def policy_uri(self, policy_uri):
        """
        Sets the policy_uri of this Client.

        :param policy_uri: The policy_uri of this Client.
        :type: str
        """

        self._policy_uri = policy_uri

    @property
    def tos_uri(self):
        """
        Gets the tos_uri of this Client.

        :return: The tos_uri of this Client.
        :rtype: str
        """
        return self._tos_uri

    @tos_uri.setter
    def tos_uri(self, tos_uri):
        """
        Sets the tos_uri of this Client.

        :param tos_uri: The tos_uri of this Client.
        :type: str
        """

        self._tos_uri = tos_uri

    @property
    def default_max_age(self):
        """
        Gets the default_max_age of this Client.

        :return: The default_max_age of this Client.
        :rtype: int
        """
        return self._default_max_age

    @default_max_age.setter
    def default_max_age(self, default_max_age):
        """
        Sets the default_max_age of this Client.

        :param default_max_age: The default_max_age of this Client.
        :type: int
        """

        self._default_max_age = default_max_age

    @property
    def default_scopes(self):
        """
        Gets the default_scopes of this Client.

        :return: The default_scopes of this Client.
        :rtype: list[str]
        """
        return self._default_scopes

    @default_scopes.setter
    def default_scopes(self, default_scopes):
        """
        Sets the default_scopes of this Client.

        :param default_scopes: The default_scopes of this Client.
        :type: list[str]
        """

        self._default_scopes = default_scopes

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Client):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
