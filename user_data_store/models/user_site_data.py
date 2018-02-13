# coding: utf-8

"""
    User Data API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class UserSiteData(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'user_id': 'str',
        'site_id': 'int',
        'data': 'object',
        'consented_at': 'date',
        'blocked': 'bool',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'user_id': 'user_id',
        'site_id': 'site_id',
        'data': 'data',
        'consented_at': 'consented_at',
        'blocked': 'blocked',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, user_id=None, site_id=None, data=None, consented_at=None, blocked=None, created_at=None, updated_at=None):  # noqa: E501
        """UserSiteData - a model defined in Swagger"""  # noqa: E501

        self._user_id = None
        self._site_id = None
        self._data = None
        self._consented_at = None
        self._blocked = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.user_id = user_id
        self.site_id = site_id
        self.data = data
        self.consented_at = consented_at
        self.blocked = blocked
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def user_id(self):
        """Gets the user_id of this UserSiteData.  # noqa: E501


        :return: The user_id of this UserSiteData.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserSiteData.


        :param user_id: The user_id of this UserSiteData.  # noqa: E501
        :type: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def site_id(self):
        """Gets the site_id of this UserSiteData.  # noqa: E501


        :return: The site_id of this UserSiteData.  # noqa: E501
        :rtype: int
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this UserSiteData.


        :param site_id: The site_id of this UserSiteData.  # noqa: E501
        :type: int
        """
        if site_id is None:
            raise ValueError("Invalid value for `site_id`, must not be `None`")  # noqa: E501

        self._site_id = site_id

    @property
    def data(self):
        """Gets the data of this UserSiteData.  # noqa: E501


        :return: The data of this UserSiteData.  # noqa: E501
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this UserSiteData.


        :param data: The data of this UserSiteData.  # noqa: E501
        :type: object
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def consented_at(self):
        """Gets the consented_at of this UserSiteData.  # noqa: E501


        :return: The consented_at of this UserSiteData.  # noqa: E501
        :rtype: date
        """
        return self._consented_at

    @consented_at.setter
    def consented_at(self, consented_at):
        """Sets the consented_at of this UserSiteData.


        :param consented_at: The consented_at of this UserSiteData.  # noqa: E501
        :type: date
        """
        if consented_at is None:
            raise ValueError("Invalid value for `consented_at`, must not be `None`")  # noqa: E501

        self._consented_at = consented_at

    @property
    def blocked(self):
        """Gets the blocked of this UserSiteData.  # noqa: E501


        :return: The blocked of this UserSiteData.  # noqa: E501
        :rtype: bool
        """
        return self._blocked

    @blocked.setter
    def blocked(self, blocked):
        """Sets the blocked of this UserSiteData.


        :param blocked: The blocked of this UserSiteData.  # noqa: E501
        :type: bool
        """
        if blocked is None:
            raise ValueError("Invalid value for `blocked`, must not be `None`")  # noqa: E501

        self._blocked = blocked

    @property
    def created_at(self):
        """Gets the created_at of this UserSiteData.  # noqa: E501


        :return: The created_at of this UserSiteData.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UserSiteData.


        :param created_at: The created_at of this UserSiteData.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this UserSiteData.  # noqa: E501


        :return: The updated_at of this UserSiteData.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this UserSiteData.


        :param updated_at: The updated_at of this UserSiteData.  # noqa: E501
        :type: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, UserSiteData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other