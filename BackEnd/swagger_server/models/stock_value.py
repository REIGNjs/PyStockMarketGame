# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class StockValue(Model):
    """
    desc: StockValue represents the value of a stock at a certain date
    author: Luca Mueller
    date: 2020-11-09
    """

    def __init__(self, id: int=None, symbol: str=None, stock_price: float=None, timestamp: datetime=None):  # noqa: E501
        """StockValue - a model defined in Swagger

        :param id: The id of this StockValue.  # noqa: E501
        :type id: int
        :param symbol: The symbol of this StockValue.  # noqa: E501
        :type symbol: str
        :param stock_price: The stock_price of this StockValue.  # noqa: E501
        :type stock_price: float
        :param timestamp: The timestamp of this StockValue.  # noqa: E501
        :type timestamp: datetime
        """
        self.swagger_types = {
            'id': int,
            'symbol': str,
            'stock_price': float,
            'timestamp': datetime
        }

        self.attribute_map = {
            'id': 'id',
            'symbol': 'symbol',
            'stock_price': 'stock_price',
            'timestamp': 'timestamp'
        }

        self._id = id
        self._symbol = symbol
        self._stock_price = stock_price
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
    def symbol(self) -> str:
        """Gets the symbol of this StockValue.


        :return: The symbol of this StockValue.
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol: str):
        """Sets the symbol of this StockValue.


        :param symbol: The symbol of this StockValue.
        :type symbol: str
        """

        self._symbol = symbol

    @property
    def stock_price(self) -> float:
        """Gets the stock_price of this StockValue.


        :return: The stock_price of this StockValue.
        :rtype: float
        """
        return self._stock_price

    @stock_price.setter
    def stock_price(self, stock_price: float):
        """Sets the stock_price of this StockValue.


        :param stock_price: The stock_price of this StockValue.
        :type stock_price: float
        """

        self._stock_price = stock_price

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
