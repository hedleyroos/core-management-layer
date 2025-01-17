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


class Invitation(object):
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
        'id': 'str',
        'invitor_id': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'email': 'str',
        'organisation_id': 'int',
        'expires_at': 'datetime',
        'invitation_redirect_url_id': 'int',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'invitor_id': 'invitor_id',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'email': 'email',
        'organisation_id': 'organisation_id',
        'expires_at': 'expires_at',
        'invitation_redirect_url_id': 'invitation_redirect_url_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, invitor_id=None, first_name=None, last_name=None, email=None, organisation_id=None, expires_at=None, invitation_redirect_url_id=None, created_at=None, updated_at=None):  # noqa: E501
        """Invitation - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._invitor_id = None
        self._first_name = None
        self._last_name = None
        self._email = None
        self._organisation_id = None
        self._expires_at = None
        self._invitation_redirect_url_id = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        self.invitor_id = invitor_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.organisation_id = organisation_id
        self.expires_at = expires_at
        if invitation_redirect_url_id is not None:
            self.invitation_redirect_url_id = invitation_redirect_url_id
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this Invitation.  # noqa: E501


        :return: The id of this Invitation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Invitation.


        :param id: The id of this Invitation.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def invitor_id(self):
        """Gets the invitor_id of this Invitation.  # noqa: E501

        The user that created the invitation  # noqa: E501

        :return: The invitor_id of this Invitation.  # noqa: E501
        :rtype: str
        """
        return self._invitor_id

    @invitor_id.setter
    def invitor_id(self, invitor_id):
        """Sets the invitor_id of this Invitation.

        The user that created the invitation  # noqa: E501

        :param invitor_id: The invitor_id of this Invitation.  # noqa: E501
        :type: str
        """
        if invitor_id is None:
            raise ValueError("Invalid value for `invitor_id`, must not be `None`")  # noqa: E501

        self._invitor_id = invitor_id

    @property
    def first_name(self):
        """Gets the first_name of this Invitation.  # noqa: E501


        :return: The first_name of this Invitation.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this Invitation.


        :param first_name: The first_name of this Invitation.  # noqa: E501
        :type: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501
        if first_name is not None and len(first_name) > 100:
            raise ValueError("Invalid value for `first_name`, length must be less than or equal to `100`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this Invitation.  # noqa: E501


        :return: The last_name of this Invitation.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this Invitation.


        :param last_name: The last_name of this Invitation.  # noqa: E501
        :type: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501
        if last_name is not None and len(last_name) > 100:
            raise ValueError("Invalid value for `last_name`, length must be less than or equal to `100`")  # noqa: E501

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this Invitation.  # noqa: E501


        :return: The email of this Invitation.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Invitation.


        :param email: The email of this Invitation.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def organisation_id(self):
        """Gets the organisation_id of this Invitation.  # noqa: E501


        :return: The organisation_id of this Invitation.  # noqa: E501
        :rtype: int
        """
        return self._organisation_id

    @organisation_id.setter
    def organisation_id(self, organisation_id):
        """Sets the organisation_id of this Invitation.


        :param organisation_id: The organisation_id of this Invitation.  # noqa: E501
        :type: int
        """
        if organisation_id is None:
            raise ValueError("Invalid value for `organisation_id`, must not be `None`")  # noqa: E501

        self._organisation_id = organisation_id

    @property
    def expires_at(self):
        """Gets the expires_at of this Invitation.  # noqa: E501


        :return: The expires_at of this Invitation.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this Invitation.


        :param expires_at: The expires_at of this Invitation.  # noqa: E501
        :type: datetime
        """
        if expires_at is None:
            raise ValueError("Invalid value for `expires_at`, must not be `None`")  # noqa: E501

        self._expires_at = expires_at

    @property
    def invitation_redirect_url_id(self):
        """Gets the invitation_redirect_url_id of this Invitation.  # noqa: E501


        :return: The invitation_redirect_url_id of this Invitation.  # noqa: E501
        :rtype: int
        """
        return self._invitation_redirect_url_id

    @invitation_redirect_url_id.setter
    def invitation_redirect_url_id(self, invitation_redirect_url_id):
        """Sets the invitation_redirect_url_id of this Invitation.


        :param invitation_redirect_url_id: The invitation_redirect_url_id of this Invitation.  # noqa: E501
        :type: int
        """

        self._invitation_redirect_url_id = invitation_redirect_url_id

    @property
    def created_at(self):
        """Gets the created_at of this Invitation.  # noqa: E501


        :return: The created_at of this Invitation.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Invitation.


        :param created_at: The created_at of this Invitation.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Invitation.  # noqa: E501


        :return: The updated_at of this Invitation.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Invitation.


        :param updated_at: The updated_at of this Invitation.  # noqa: E501
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
        if not isinstance(other, Invitation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
