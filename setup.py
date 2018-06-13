# coding: utf-8

from setuptools import setup, find_packages
from management_layer import __version__

NAME = "management_layer"
VERSION = __version__

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]
LONG_DESCRIPTION_FILES = ["README.rst", "AUTHORS.rst", "CHANGELOG.rst"]

setup(
    name=NAME,
    version=VERSION,
    description="Girl Effect Core Managment Layer",
    long_description="".join(open(filename, "r").read() for filename in LONG_DESCRIPTION_FILES),
    author_email="dev@praekelt.com",
    url="http://github.com/girleffect/core-management-layer",
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True
)
