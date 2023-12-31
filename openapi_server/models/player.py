from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class Player(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, name=None, key=None):  # noqa: E501
        """Player - a model defined in OpenAPI

        :param id: The id of this Player.  # noqa: E501
        :type id: int
        :param name: The name of this Player.  # noqa: E501
        :type name: str
        :param key: The key of this Player.  # noqa: E501
        :type key: str
        """
        self.openapi_types = {
            'id': int,
            'name': str,
            'key': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'key': 'key'
        }

        self._id = id
        self._name = name
        self._key = key

    @classmethod
    def from_dict(cls, dikt) -> 'Player':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Player of this Player.  # noqa: E501
        :rtype: Player
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Player.


        :return: The id of this Player.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Player.


        :param id: The id of this Player.
        :type id: int
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this Player.


        :return: The name of this Player.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Player.


        :param name: The name of this Player.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def key(self) -> str:
        """Gets the key of this Player.

        Identify the player against the server  # noqa: E501

        :return: The key of this Player.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key: str):
        """Sets the key of this Player.

        Identify the player against the server  # noqa: E501

        :param key: The key of this Player.
        :type key: str
        """

        self._key = key
