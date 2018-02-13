# coding: utf-8

# flake8: noqa
"""
    Authentication Service API

    This is the API that will be exposed by the Authentication Service.  The Authentication Service facilitates user registration and login via web-based flows as defined for the OpenID Connect specification.   # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from authentication_service.models.address import Address
from authentication_service.models.client import Client
from authentication_service.models.content import Content
from authentication_service.models.o_auth2_error import OAuth2Error
from authentication_service.models.problem_detail import ProblemDetail
from authentication_service.models.session import Session
from authentication_service.models.token import Token
from authentication_service.models.user import User
from authentication_service.models.user_info import UserInfo
from authentication_service.models.user_update import UserUpdate