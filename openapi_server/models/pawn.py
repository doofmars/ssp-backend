from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class Pawn(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, item=None, owner=None):  # noqa: E501
        """Pawn - a model defined in OpenAPI

        :param item: The item of this Pawn.  # noqa: E501
        :type item: str
        :param owner: The owner of this Pawn.  # noqa: E501
        :type owner: str
        """
        self.openapi_types = {
            'item': str,
            'owner': str
        }

        self.attribute_map = {
            'item': 'item',
            'owner': 'owner'
        }

        self._item = item
        self._owner = owner

    @classmethod
    def from_dict(cls, dikt) -> 'Pawn':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Pawn of this Pawn.  # noqa: E501
        :rtype: Pawn
        """
        return util.deserialize_model(dikt, cls)

    @property
    def item(self) -> str:
        """Gets the item of this Pawn.


        :return: The item of this Pawn.
        :rtype: str
        """
        return self._item

    @item.setter
    def item(self, item: str):
        """Sets the item of this Pawn.


        :param item: The item of this Pawn.
        :type item: str
        """
        allowed_values = ["ROCK", "PAPER", "SCISSORS", "TRAP", "FLAG", "EMPTY"]  # noqa: E501
        if item not in allowed_values:
            raise ValueError(
                "Invalid value for `item` ({0}), must be one of {1}"
                .format(item, allowed_values)
            )

        self._item = item

    @property
    def owner(self) -> str:
        """Gets the owner of this Pawn.


        :return: The owner of this Pawn.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner: str):
        """Sets the owner of this Pawn.


        :param owner: The owner of this Pawn.
        :type owner: str
        """
        allowed_values = ["HOST", "GUEST"]  # noqa: E501
        if owner not in allowed_values:
            raise ValueError(
                "Invalid value for `owner` ({0}), must be one of {1}"
                .format(owner, allowed_values)
            )

        self._owner = owner
