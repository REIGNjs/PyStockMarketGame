# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class StockValue(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, wkn: str=None, market_value: float=None, timestamp: datetime=None):  # noqa: E501
        """StockValue - a model defined in Swagger

        :param id: The id of this StockValue.  # noqa: E501
        :type id: int
        :param wkn: The wkn of this StockValue.  # noqa: E501
        :type wkn: str
        :param market_value: The market_value of this StockValue.  # noqa: E501
        :type market_value: float
        :param timestamp: The timestamp of this StockValue.  # noqa: E501
        :type timestamp: datetime
        """
        self.swagger_types = {
            'id': int,
            'wkn': str,
            'market_value': float,
            'timestamp': datetime
        }

        self.attribute_map = {
            'id': 'id',
            'wkn': 'wkn',
            'market_value': 'marketValue',
            'timestamp': 'timestamp'
        }

        self._id = id
        self._wkn = wkn
        self._market_value = market_value
        self._timestamp = timestamp

    @classmethod
    def from_dict(cls, dikt) -> 'StockValue':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The StockValue of this StockValue.  # noqa: E501
        :rtype: StockValue
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this StockValue.


        :return: The id of this StockValue.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this StockValue.


        :param id: The id of this StockValue.
        :type id: int
        """

        self._id = id

    @property
    def wkn(self) -> str:
        """Gets the wkn of this StockValue.


        :return: The wkn of this StockValue.
        :rtype: str
        """
        return self._wkn

    @wkn.setter
    def wkn(self, wkn: str):
        """Sets the wkn of this StockValue.


        :param wkn: The wkn of this StockValue.
        :type wkn: str
        """

        self._wkn = wkn

    @property
    def market_value(self) -> float:
        """Gets the market_value of this StockValue.


        :return: The market_value of this StockValue.
        :rtype: float
        """
        return self._market_value

    @market_value.setter
    def market_value(self, market_value: float):
        """Sets the market_value of this StockValue.


        :param market_value: The market_value of this StockValue.
        :type market_value: float
        """

        self._market_value = market_value

    @property
    def timestamp(self) -> datetime:
        """Gets the timestamp of this StockValue.


        :return: The timestamp of this StockValue.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: datetime):
        """Sets the timestamp of this StockValue.


        :param timestamp: The timestamp of this StockValue.
        :type timestamp: datetime
        """

        self._timestamp = timestamp
