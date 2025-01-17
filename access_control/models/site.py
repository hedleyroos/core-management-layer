# coding: utf-8

"""
    Access Control API

    # The Access Control API  ## Overview The Access Control API is an API exposed to other core components. It uses an API Key in an HTTP header to perform authentication and authorisation.  Most of the API calls facilitates CRUD of the entities defined in the Access Control component. Others calls allows the retrieval of information in a form that is convenient for other components (most notably the Management Layer) to consume.   # noqa: E501

    OpenAPI spec version: 
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Site(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'int',
        'name': 'str',
        'client_id': 'int',
        'domain_id': 'int',
        'description': 'str',
        'is_active': 'bool',
        'deletion_method_id': 'int',
        'deletion_method_data': 'object',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'client_id': 'client_id',
        'domain_id': 'domain_id',
        'description': 'description',
        'is_active': 'is_active',
        'deletion_method_id': 'deletion_method_id',
        'deletion_method_data': 'deletion_method_data',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, client_id=None, domain_id=None, description=None, is_active=None, deletion_method_id=None, deletion_method_data=None, created_at=None, updated_at=None):  # noqa: E501
        """Site - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._name = None
        self._client_id = None
        self._domain_id = None
        self._description = None
        self._is_active = None
        self._deletion_method_id = None
        self._deletion_method_data = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        self.name = name
        if client_id is not None:
            self.client_id = client_id
        self.domain_id = domain_id
        if description is not None:
            self.description = description
        self.is_active = is_active
        self.deletion_method_id = deletion_method_id
        self.deletion_method_data = deletion_method_data
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this Site.  # noqa: E501


        :return: The id of this Site.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Site.


        :param id: The id of this Site.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Site.  # noqa: E501


        :return: The name of this Site.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Site.


        :param name: The name of this Site.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 30:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `30`")  # noqa: E501

        self._name = name

    @property
    def client_id(self):
        """Gets the client_id of this Site.  # noqa: E501


        :return: The client_id of this Site.  # noqa: E501
        :rtype: int
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this Site.


        :param client_id: The client_id of this Site.  # noqa: E501
        :type: int
        """

        self._client_id = client_id

    @property
    def domain_id(self):
        """Gets the domain_id of this Site.  # noqa: E501


        :return: The domain_id of this Site.  # noqa: E501
        :rtype: int
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this Site.


        :param domain_id: The domain_id of this Site.  # noqa: E501
        :type: int
        """
        if domain_id is None:
            raise ValueError("Invalid value for `domain_id`, must not be `None`")  # noqa: E501

        self._domain_id = domain_id

    @property
    def description(self):
        """Gets the description of this Site.  # noqa: E501


        :return: The description of this Site.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Site.


        :param description: The description of this Site.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def is_active(self):
        """Gets the is_active of this Site.  # noqa: E501


        :return: The is_active of this Site.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this Site.


        :param is_active: The is_active of this Site.  # noqa: E501
        :type: bool
        """
        if is_active is None:
            raise ValueError("Invalid value for `is_active`, must not be `None`")  # noqa: E501

        self._is_active = is_active

    @property
    def deletion_method_id(self):
        """Gets the deletion_method_id of this Site.  # noqa: E501


        :return: The deletion_method_id of this Site.  # noqa: E501
        :rtype: int
        """
        return self._deletion_method_id

    @deletion_method_id.setter
    def deletion_method_id(self, deletion_method_id):
        """Sets the deletion_method_id of this Site.


        :param deletion_method_id: The deletion_method_id of this Site.  # noqa: E501
        :type: int
        """
        if deletion_method_id is None:
            raise ValueError("Invalid value for `deletion_method_id`, must not be `None`")  # noqa: E501

        self._deletion_method_id = deletion_method_id

    @property
    def deletion_method_data(self):
        """Gets the deletion_method_data of this Site.  # noqa: E501


        :return: The deletion_method_data of this Site.  # noqa: E501
        :rtype: object
        """
        return self._deletion_method_data

    @deletion_method_data.setter
    def deletion_method_data(self, deletion_method_data):
        """Sets the deletion_method_data of this Site.


        :param deletion_method_data: The deletion_method_data of this Site.  # noqa: E501
        :type: object
        """
        if deletion_method_data is None:
            raise ValueError("Invalid value for `deletion_method_data`, must not be `None`")  # noqa: E501

        self._deletion_method_data = deletion_method_data

    @property
    def created_at(self):
        """Gets the created_at of this Site.  # noqa: E501


        :return: The created_at of this Site.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Site.


        :param created_at: The created_at of this Site.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Site.  # noqa: E501


        :return: The updated_at of this Site.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Site.


        :param updated_at: The updated_at of this Site.  # noqa: E501
        :type: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Site):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
