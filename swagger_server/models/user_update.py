# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class UserUpdate(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, first_name: str=None, last_name: str=None, email: str=None, is_active: bool=None, email_verified: bool=None, msisdn_verified: bool=None, msisdn: str=None, gender: str=None, birth_date: date=None, avatar: str=None, country_code: str=None):
        """
        UserUpdate - a model defined in Swagger

        :param first_name: The first_name of this UserUpdate.
        :type first_name: str
        :param last_name: The last_name of this UserUpdate.
        :type last_name: str
        :param email: The email of this UserUpdate.
        :type email: str
        :param is_active: The is_active of this UserUpdate.
        :type is_active: bool
        :param email_verified: The email_verified of this UserUpdate.
        :type email_verified: bool
        :param msisdn_verified: The msisdn_verified of this UserUpdate.
        :type msisdn_verified: bool
        :param msisdn: The msisdn of this UserUpdate.
        :type msisdn: str
        :param gender: The gender of this UserUpdate.
        :type gender: str
        :param birth_date: The birth_date of this UserUpdate.
        :type birth_date: date
        :param avatar: The avatar of this UserUpdate.
        :type avatar: str
        :param country_code: The country_code of this UserUpdate.
        :type country_code: str
        """
        self.swagger_types = {
            'first_name': str,
            'last_name': str,
            'email': str,
            'is_active': bool,
            'email_verified': bool,
            'msisdn_verified': bool,
            'msisdn': str,
            'gender': str,
            'birth_date': date,
            'avatar': str,
            'country_code': str
        }

        self.attribute_map = {
            'first_name': 'first_name',
            'last_name': 'last_name',
            'email': 'email',
            'is_active': 'is_active',
            'email_verified': 'email_verified',
            'msisdn_verified': 'msisdn_verified',
            'msisdn': 'msisdn',
            'gender': 'gender',
            'birth_date': 'birth_date',
            'avatar': 'avatar',
            'country_code': 'country_code'
        }

        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._is_active = is_active
        self._email_verified = email_verified
        self._msisdn_verified = msisdn_verified
        self._msisdn = msisdn
        self._gender = gender
        self._birth_date = birth_date
        self._avatar = avatar
        self._country_code = country_code

    @classmethod
    def from_dict(cls, dikt) -> 'UserUpdate':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The user_update of this UserUpdate.
        :rtype: UserUpdate
        """
        return deserialize_model(dikt, cls)

    @property
    def first_name(self) -> str:
        """
        Gets the first_name of this UserUpdate.
        

        :return: The first_name of this UserUpdate.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        """
        Sets the first_name of this UserUpdate.
        

        :param first_name: The first_name of this UserUpdate.
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def last_name(self) -> str:
        """
        Gets the last_name of this UserUpdate.
        

        :return: The last_name of this UserUpdate.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """
        Sets the last_name of this UserUpdate.
        

        :param last_name: The last_name of this UserUpdate.
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def email(self) -> str:
        """
        Gets the email of this UserUpdate.
        

        :return: The email of this UserUpdate.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """
        Sets the email of this UserUpdate.
        

        :param email: The email of this UserUpdate.
        :type email: str
        """

        self._email = email

    @property
    def is_active(self) -> bool:
        """
        Gets the is_active of this UserUpdate.
        Designates whether this user should be treated as active. Deselect this instead of deleting accounts.

        :return: The is_active of this UserUpdate.
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active: bool):
        """
        Sets the is_active of this UserUpdate.
        Designates whether this user should be treated as active. Deselect this instead of deleting accounts.

        :param is_active: The is_active of this UserUpdate.
        :type is_active: bool
        """

        self._is_active = is_active

    @property
    def email_verified(self) -> bool:
        """
        Gets the email_verified of this UserUpdate.

        :return: The email_verified of this UserUpdate.
        :rtype: bool
        """
        return self._email_verified

    @email_verified.setter
    def email_verified(self, email_verified: bool):
        """
        Sets the email_verified of this UserUpdate.

        :param email_verified: The email_verified of this UserUpdate.
        :type email_verified: bool
        """

        self._email_verified = email_verified

    @property
    def msisdn_verified(self) -> bool:
        """
        Gets the msisdn_verified of this UserUpdate.

        :return: The msisdn_verified of this UserUpdate.
        :rtype: bool
        """
        return self._msisdn_verified

    @msisdn_verified.setter
    def msisdn_verified(self, msisdn_verified: bool):
        """
        Sets the msisdn_verified of this UserUpdate.

        :param msisdn_verified: The msisdn_verified of this UserUpdate.
        :type msisdn_verified: bool
        """

        self._msisdn_verified = msisdn_verified

    @property
    def msisdn(self) -> str:
        """
        Gets the msisdn of this UserUpdate.

        :return: The msisdn of this UserUpdate.
        :rtype: str
        """
        return self._msisdn

    @msisdn.setter
    def msisdn(self, msisdn: str):
        """
        Sets the msisdn of this UserUpdate.

        :param msisdn: The msisdn of this UserUpdate.
        :type msisdn: str
        """
        if msisdn is not None and len(msisdn) > 15:
            raise ValueError("Invalid value for `msisdn`, length must be less than or equal to `15`")

        self._msisdn = msisdn

    @property
    def gender(self) -> str:
        """
        Gets the gender of this UserUpdate.

        :return: The gender of this UserUpdate.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender: str):
        """
        Sets the gender of this UserUpdate.

        :param gender: The gender of this UserUpdate.
        :type gender: str
        """

        self._gender = gender

    @property
    def birth_date(self) -> date:
        """
        Gets the birth_date of this UserUpdate.

        :return: The birth_date of this UserUpdate.
        :rtype: date
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date: date):
        """
        Sets the birth_date of this UserUpdate.

        :param birth_date: The birth_date of this UserUpdate.
        :type birth_date: date
        """

        self._birth_date = birth_date

    @property
    def avatar(self) -> str:
        """
        Gets the avatar of this UserUpdate.

        :return: The avatar of this UserUpdate.
        :rtype: str
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar: str):
        """
        Sets the avatar of this UserUpdate.

        :param avatar: The avatar of this UserUpdate.
        :type avatar: str
        """

        self._avatar = avatar

    @property
    def country_code(self) -> str:
        """
        Gets the country_code of this UserUpdate.

        :return: The country_code of this UserUpdate.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code: str):
        """
        Sets the country_code of this UserUpdate.

        :param country_code: The country_code of this UserUpdate.
        :type country_code: str
        """
        if country_code is not None and len(country_code) > 2:
            raise ValueError("Invalid value for `country_code`, length must be less than or equal to `2`")

        self._country_code = country_code

