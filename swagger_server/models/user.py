# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class User(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id: str=None, username: str=None, first_name: str=None, last_name: str=None, email: str=None, is_active: bool=None, date_joined: date=None, last_login: str=None, email_verified: bool=None, msisdn_verified: bool=None, msisdn: str=None, gender: str=None, birth_date: date=None, avatar: str=None, country_code: str=None, created_at: datetime=None, updated_at: datetime=None):
        """
        User - a model defined in Swagger

        :param id: The id of this User.
        :type id: str
        :param username: The username of this User.
        :type username: str
        :param first_name: The first_name of this User.
        :type first_name: str
        :param last_name: The last_name of this User.
        :type last_name: str
        :param email: The email of this User.
        :type email: str
        :param is_active: The is_active of this User.
        :type is_active: bool
        :param date_joined: The date_joined of this User.
        :type date_joined: date
        :param last_login: The last_login of this User.
        :type last_login: str
        :param email_verified: The email_verified of this User.
        :type email_verified: bool
        :param msisdn_verified: The msisdn_verified of this User.
        :type msisdn_verified: bool
        :param msisdn: The msisdn of this User.
        :type msisdn: str
        :param gender: The gender of this User.
        :type gender: str
        :param birth_date: The birth_date of this User.
        :type birth_date: date
        :param avatar: The avatar of this User.
        :type avatar: str
        :param country_code: The country_code of this User.
        :type country_code: str
        :param created_at: The created_at of this User.
        :type created_at: datetime
        :param updated_at: The updated_at of this User.
        :type updated_at: datetime
        """
        self.swagger_types = {
            'id': str,
            'username': str,
            'first_name': str,
            'last_name': str,
            'email': str,
            'is_active': bool,
            'date_joined': date,
            'last_login': str,
            'email_verified': bool,
            'msisdn_verified': bool,
            'msisdn': str,
            'gender': str,
            'birth_date': date,
            'avatar': str,
            'country_code': str,
            'created_at': datetime,
            'updated_at': datetime
        }

        self.attribute_map = {
            'id': 'id',
            'username': 'username',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'email': 'email',
            'is_active': 'is_active',
            'date_joined': 'date_joined',
            'last_login': 'last_login',
            'email_verified': 'email_verified',
            'msisdn_verified': 'msisdn_verified',
            'msisdn': 'msisdn',
            'gender': 'gender',
            'birth_date': 'birth_date',
            'avatar': 'avatar',
            'country_code': 'country_code',
            'created_at': 'created_at',
            'updated_at': 'updated_at'
        }

        self._id = id
        self._username = username
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._is_active = is_active
        self._date_joined = date_joined
        self._last_login = last_login
        self._email_verified = email_verified
        self._msisdn_verified = msisdn_verified
        self._msisdn = msisdn
        self._gender = gender
        self._birth_date = birth_date
        self._avatar = avatar
        self._country_code = country_code
        self._created_at = created_at
        self._updated_at = updated_at

    @classmethod
    def from_dict(cls, dikt) -> 'User':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The user of this User.
        :rtype: User
        """
        return deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """
        Gets the id of this User.
        The UUID of the user

        :return: The id of this User.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """
        Sets the id of this User.
        The UUID of the user

        :param id: The id of this User.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def username(self) -> str:
        """
        Gets the username of this User.
        Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.

        :return: The username of this User.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """
        Sets the username of this User.
        Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.

        :param username: The username of this User.
        :type username: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")

        self._username = username

    @property
    def first_name(self) -> str:
        """
        Gets the first_name of this User.
        

        :return: The first_name of this User.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        """
        Sets the first_name of this User.
        

        :param first_name: The first_name of this User.
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def last_name(self) -> str:
        """
        Gets the last_name of this User.
        

        :return: The last_name of this User.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """
        Sets the last_name of this User.
        

        :param last_name: The last_name of this User.
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def email(self) -> str:
        """
        Gets the email of this User.
        

        :return: The email of this User.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """
        Sets the email of this User.
        

        :param email: The email of this User.
        :type email: str
        """

        self._email = email

    @property
    def is_active(self) -> bool:
        """
        Gets the is_active of this User.
        Designates whether this user should be treated as active. Deselect this instead of deleting accounts.

        :return: The is_active of this User.
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active: bool):
        """
        Sets the is_active of this User.
        Designates whether this user should be treated as active. Deselect this instead of deleting accounts.

        :param is_active: The is_active of this User.
        :type is_active: bool
        """
        if is_active is None:
            raise ValueError("Invalid value for `is_active`, must not be `None`")

        self._is_active = is_active

    @property
    def date_joined(self) -> date:
        """
        Gets the date_joined of this User.
        

        :return: The date_joined of this User.
        :rtype: date
        """
        return self._date_joined

    @date_joined.setter
    def date_joined(self, date_joined: date):
        """
        Sets the date_joined of this User.
        

        :param date_joined: The date_joined of this User.
        :type date_joined: date
        """
        if date_joined is None:
            raise ValueError("Invalid value for `date_joined`, must not be `None`")

        self._date_joined = date_joined

    @property
    def last_login(self) -> str:
        """
        Gets the last_login of this User.
        

        :return: The last_login of this User.
        :rtype: str
        """
        return self._last_login

    @last_login.setter
    def last_login(self, last_login: str):
        """
        Sets the last_login of this User.
        

        :param last_login: The last_login of this User.
        :type last_login: str
        """

        self._last_login = last_login

    @property
    def email_verified(self) -> bool:
        """
        Gets the email_verified of this User.

        :return: The email_verified of this User.
        :rtype: bool
        """
        return self._email_verified

    @email_verified.setter
    def email_verified(self, email_verified: bool):
        """
        Sets the email_verified of this User.

        :param email_verified: The email_verified of this User.
        :type email_verified: bool
        """

        self._email_verified = email_verified

    @property
    def msisdn_verified(self) -> bool:
        """
        Gets the msisdn_verified of this User.

        :return: The msisdn_verified of this User.
        :rtype: bool
        """
        return self._msisdn_verified

    @msisdn_verified.setter
    def msisdn_verified(self, msisdn_verified: bool):
        """
        Sets the msisdn_verified of this User.

        :param msisdn_verified: The msisdn_verified of this User.
        :type msisdn_verified: bool
        """

        self._msisdn_verified = msisdn_verified

    @property
    def msisdn(self) -> str:
        """
        Gets the msisdn of this User.

        :return: The msisdn of this User.
        :rtype: str
        """
        return self._msisdn

    @msisdn.setter
    def msisdn(self, msisdn: str):
        """
        Sets the msisdn of this User.

        :param msisdn: The msisdn of this User.
        :type msisdn: str
        """
        if msisdn is not None and len(msisdn) > 15:
            raise ValueError("Invalid value for `msisdn`, length must be less than or equal to `15`")

        self._msisdn = msisdn

    @property
    def gender(self) -> str:
        """
        Gets the gender of this User.

        :return: The gender of this User.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender: str):
        """
        Sets the gender of this User.

        :param gender: The gender of this User.
        :type gender: str
        """

        self._gender = gender

    @property
    def birth_date(self) -> date:
        """
        Gets the birth_date of this User.

        :return: The birth_date of this User.
        :rtype: date
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date: date):
        """
        Sets the birth_date of this User.

        :param birth_date: The birth_date of this User.
        :type birth_date: date
        """

        self._birth_date = birth_date

    @property
    def avatar(self) -> str:
        """
        Gets the avatar of this User.

        :return: The avatar of this User.
        :rtype: str
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar: str):
        """
        Sets the avatar of this User.

        :param avatar: The avatar of this User.
        :type avatar: str
        """

        self._avatar = avatar

    @property
    def country_code(self) -> str:
        """
        Gets the country_code of this User.

        :return: The country_code of this User.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code: str):
        """
        Sets the country_code of this User.

        :param country_code: The country_code of this User.
        :type country_code: str
        """
        if country_code is not None and len(country_code) > 2:
            raise ValueError("Invalid value for `country_code`, length must be less than or equal to `2`")

        self._country_code = country_code

    @property
    def created_at(self) -> datetime:
        """
        Gets the created_at of this User.

        :return: The created_at of this User.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: datetime):
        """
        Sets the created_at of this User.

        :param created_at: The created_at of this User.
        :type created_at: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")

        self._created_at = created_at

    @property
    def updated_at(self) -> datetime:
        """
        Gets the updated_at of this User.

        :return: The updated_at of this User.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at: datetime):
        """
        Sets the updated_at of this User.

        :param updated_at: The updated_at of this User.
        :type updated_at: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")

        self._updated_at = updated_at

