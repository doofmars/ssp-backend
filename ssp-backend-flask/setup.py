# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion",
    "swagger-ui-bundle>=0.0.2"
]

setup(
    name=NAME,
    version=VERSION,
    description="SSP-Online Backend",
    author_email="",
    url="",
    keywords=["Swagger", "SSP-Online Backend"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    This is a the backend for the SSP Online Game. It is a RESTful API that is used by the frontend to play the game.  Some useful links: - [ssp-online](https://github.com/doofmars/ssp-online) - The source code for the SSP Online Game - [ssp-backend](https://github.com/doofmars/ssp-backend) - The source code for the SSP Backend
    """
)
