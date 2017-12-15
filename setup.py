# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "management_layer"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="Girl Effect Core Managment Layer",
    long_description=open("README.rst", "r").read() + open("AUTHORS.rst", "r").read() + open("CHANGELOG.rst", "r").read(),
    author_email="dev@praekelt.com",
    url="http://github.com/girleffect/core-management-layer",
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    long_description="""\
    The Management Layer API exposes the functionality that is available to users. Access to this API is based on a user token that must be presented with every request.  The Management Layer ties together the User Data Store, Access Control System and Authentication Service. It performs permission checking and audit logging.
    """
)

