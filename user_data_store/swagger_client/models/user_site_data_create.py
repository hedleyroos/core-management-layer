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


class UserSiteDataCreate(object):
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
        'blocked': 'bool'
    }

    attribute_map = {
        'user_id': 'user_id',
        'site_id': 'site_id',
        'data': 'data',
        'consented_at': 'consented_at',
        'blocked': 'blocked'
    }

    def __init__(self, user_id=None, site_id=None, data=None, consented_at=None, blocked=None):  # noqa: E501
        """UserSiteDataCreate - a model defined in Swagger"""  # noqa: E501

        self._user_id = None
        self._site_id = None
        self._data = None
        self._consented_at = None
        self._blocked = None
        self.discriminator = None

        self.user_id = user_id
        self.site_id = site_id
        self.data = data
        if consented_at is not None:
            self.consented_at = consented_at
        if blocked is not None:
            self.blocked = blocked

    @property
    def user_id(self):
        """Gets the user_id of this UserSiteDataCreate.  # noqa: E501


        :return: The user_id of this UserSiteDataCreate.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserSiteDataCreate.


        :param user_id: The user_id of this UserSiteDataCreate.  # noqa: E501
        :type: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def site_id(self):
        """Gets the site_id of this UserSiteDataCreate.  # noqa: E501


        :return: The site_id of this UserSiteDataCreate.  # noqa: E501
        :rtype: int
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this UserSiteDataCreate.


        :param site_id: The site_id of this UserSiteDataCreate.  # noqa: E501
        :type: int
        """
        if site_id is None:
            raise ValueError("Invalid value for `site_id`, must not be `None`")  # noqa: E501

        self._site_id = site_id

    @property
    def data(self):
        """Gets the data of this UserSiteDataCreate.  # noqa: E501


        :return: The data of this UserSiteDataCreate.  # noqa: E501
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this UserSiteDataCreate.


        :param data: The data of this UserSiteDataCreate.  # noqa: E501
        :type: object
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def consented_at(self):
        """Gets the consented_at of this UserSiteDataCreate.  # noqa: E501


        :return: The consented_at of this UserSiteDataCreate.  # noqa: E501
        :rtype: date
        """
        return self._consented_at

    @consented_at.setter
    def consented_at(self, consented_at):
        """Sets the consented_at of this UserSiteDataCreate.


        :param consented_at: The consented_at of this UserSiteDataCreate.  # noqa: E501
        :type: date
        """

        self._consented_at = consented_at

    @property
    def blocked(self):
        """Gets the blocked of this UserSiteDataCreate.  # noqa: E501


        :return: The blocked of this UserSiteDataCreate.  # noqa: E501
        :rtype: bool
        """
        return self._blocked

    @blocked.setter
    def blocked(self, blocked):
        """Sets the blocked of this UserSiteDataCreate.


        :param blocked: The blocked of this UserSiteDataCreate.  # noqa: E501
        :type: bool
        """

        self._blocked = blocked

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
        if not isinstance(other, UserSiteDataCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
