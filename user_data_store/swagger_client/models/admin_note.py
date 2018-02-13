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


class AdminNote(object):
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
        'id': 'int',
        'user_id': 'str',
        'creator_id': 'str',
        'note': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'user_id': 'user_id',
        'creator_id': 'creator_id',
        'note': 'note',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, user_id=None, creator_id=None, note=None, created_at=None, updated_at=None):  # noqa: E501
        """AdminNote - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._user_id = None
        self._creator_id = None
        self._note = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        self.user_id = user_id
        self.creator_id = creator_id
        self.note = note
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this AdminNote.  # noqa: E501


        :return: The id of this AdminNote.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AdminNote.


        :param id: The id of this AdminNote.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def user_id(self):
        """Gets the user_id of this AdminNote.  # noqa: E501


        :return: The user_id of this AdminNote.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AdminNote.


        :param user_id: The user_id of this AdminNote.  # noqa: E501
        :type: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def creator_id(self):
        """Gets the creator_id of this AdminNote.  # noqa: E501


        :return: The creator_id of this AdminNote.  # noqa: E501
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this AdminNote.


        :param creator_id: The creator_id of this AdminNote.  # noqa: E501
        :type: str
        """
        if creator_id is None:
            raise ValueError("Invalid value for `creator_id`, must not be `None`")  # noqa: E501

        self._creator_id = creator_id

    @property
    def note(self):
        """Gets the note of this AdminNote.  # noqa: E501


        :return: The note of this AdminNote.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this AdminNote.


        :param note: The note of this AdminNote.  # noqa: E501
        :type: str
        """
        if note is None:
            raise ValueError("Invalid value for `note`, must not be `None`")  # noqa: E501

        self._note = note

    @property
    def created_at(self):
        """Gets the created_at of this AdminNote.  # noqa: E501


        :return: The created_at of this AdminNote.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AdminNote.


        :param created_at: The created_at of this AdminNote.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this AdminNote.  # noqa: E501


        :return: The updated_at of this AdminNote.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this AdminNote.


        :param updated_at: The updated_at of this AdminNote.  # noqa: E501
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
        if not isinstance(other, AdminNote):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other