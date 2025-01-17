# coding: utf-8

"""
    Authentication Service API

    This is the API that will be exposed by the Authentication Service. The Authentication Service facilitates user registration and login via web-based flows as defined for the OpenID Connect specification.   # noqa: E501

    OpenAPI spec version: 1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class RequestUserDeletion(object):
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
        'user_id': 'str',
        'deleter_id': 'str',
        'reason': 'str'
    }

    attribute_map = {
        'user_id': 'user_id',
        'deleter_id': 'deleter_id',
        'reason': 'reason'
    }

    def __init__(self, user_id=None, deleter_id=None, reason=None):  # noqa: E501
        """RequestUserDeletion - a model defined in OpenAPI"""  # noqa: E501

        self._user_id = None
        self._deleter_id = None
        self._reason = None
        self.discriminator = None

        self.user_id = user_id
        self.deleter_id = deleter_id
        self.reason = reason

    @property
    def user_id(self):
        """Gets the user_id of this RequestUserDeletion.  # noqa: E501


        :return: The user_id of this RequestUserDeletion.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this RequestUserDeletion.


        :param user_id: The user_id of this RequestUserDeletion.  # noqa: E501
        :type: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def deleter_id(self):
        """Gets the deleter_id of this RequestUserDeletion.  # noqa: E501


        :return: The deleter_id of this RequestUserDeletion.  # noqa: E501
        :rtype: str
        """
        return self._deleter_id

    @deleter_id.setter
    def deleter_id(self, deleter_id):
        """Sets the deleter_id of this RequestUserDeletion.


        :param deleter_id: The deleter_id of this RequestUserDeletion.  # noqa: E501
        :type: str
        """
        if deleter_id is None:
            raise ValueError("Invalid value for `deleter_id`, must not be `None`")  # noqa: E501

        self._deleter_id = deleter_id

    @property
    def reason(self):
        """Gets the reason of this RequestUserDeletion.  # noqa: E501


        :return: The reason of this RequestUserDeletion.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this RequestUserDeletion.


        :param reason: The reason of this RequestUserDeletion.  # noqa: E501
        :type: str
        """
        if reason is None:
            raise ValueError("Invalid value for `reason`, must not be `None`")  # noqa: E501

        self._reason = reason

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
        if not isinstance(other, RequestUserDeletion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
