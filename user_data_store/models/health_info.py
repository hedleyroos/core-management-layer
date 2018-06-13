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


class HealthInfo(object):
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
        'host': 'str',
        'server_timestamp': 'datetime',
        'version': 'str',
        'db_timestamp': 'datetime'
    }

    attribute_map = {
        'host': 'host',
        'server_timestamp': 'server_timestamp',
        'version': 'version',
        'db_timestamp': 'db_timestamp'
    }

    def __init__(self, host=None, server_timestamp=None, version=None, db_timestamp=None):  # noqa: E501
        """HealthInfo - a model defined in Swagger"""  # noqa: E501

        self._host = None
        self._server_timestamp = None
        self._version = None
        self._db_timestamp = None
        self.discriminator = None

        self.host = host
        self.server_timestamp = server_timestamp
        self.version = version
        self.db_timestamp = db_timestamp

    @property
    def host(self):
        """Gets the host of this HealthInfo.  # noqa: E501


        :return: The host of this HealthInfo.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this HealthInfo.


        :param host: The host of this HealthInfo.  # noqa: E501
        :type: str
        """
        if host is None:
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def server_timestamp(self):
        """Gets the server_timestamp of this HealthInfo.  # noqa: E501


        :return: The server_timestamp of this HealthInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._server_timestamp

    @server_timestamp.setter
    def server_timestamp(self, server_timestamp):
        """Sets the server_timestamp of this HealthInfo.


        :param server_timestamp: The server_timestamp of this HealthInfo.  # noqa: E501
        :type: datetime
        """
        if server_timestamp is None:
            raise ValueError("Invalid value for `server_timestamp`, must not be `None`")  # noqa: E501

        self._server_timestamp = server_timestamp

    @property
    def version(self):
        """Gets the version of this HealthInfo.  # noqa: E501


        :return: The version of this HealthInfo.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this HealthInfo.


        :param version: The version of this HealthInfo.  # noqa: E501
        :type: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def db_timestamp(self):
        """Gets the db_timestamp of this HealthInfo.  # noqa: E501


        :return: The db_timestamp of this HealthInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._db_timestamp

    @db_timestamp.setter
    def db_timestamp(self, db_timestamp):
        """Sets the db_timestamp of this HealthInfo.


        :param db_timestamp: The db_timestamp of this HealthInfo.  # noqa: E501
        :type: datetime
        """
        if db_timestamp is None:
            raise ValueError("Invalid value for `db_timestamp`, must not be `None`")  # noqa: E501

        self._db_timestamp = db_timestamp

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
        if not isinstance(other, HealthInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
