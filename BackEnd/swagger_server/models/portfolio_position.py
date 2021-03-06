# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.stock_value import StockValue
from swagger_server.models.base_model_ import Model
from swagger_server import util


class PortfolioPosition(Model):
    """
    desc: PortfolioPosition represents a stock asset in the users portfolio
    author: Luca Mueller
    date: 2020-11-09
    """

    def __init__(self, symbol: str=None, stock_name: str=None, logo_url: str=None, amount: int=None, stock_value: StockValue=None, stock_buyin_price: float=None):  # noqa: E501
        """PortfolioPosition - a model defined in Swagger

        :param symbol: The symbol of this PortfolioPosition.  # noqa: E501
        :type symbol: str
        :param stock_name: The stock_name of this PortfolioPosition.  # noqa: E501
        :type stock_name: str
        :param logo_url: The logo_url of this PortfolioPosition.  # noqa: E501
        :type logo_url: str
        :param amount: The amount of this PortfolioPosition.  # noqa: E501
        :type amount: int
        :param stock_value: The stock_value of this PortfolioPosition.  # noqa: E501
        :type stock_value: StockValue
        :param stock_buyin_price: The stock_buyin_price of this PortfolioPosition.  # noqa: E501
        :type stock_buyin_price: float
        """
        self.swagger_types = {
            'symbol': str,
            'stock_name': str,
            'logo_url': str,
            'amount': int,
            'stock_value': StockValue,
            'stock_buyin_price': float
        }

        self.attribute_map = {
            'symbol': 'symbol',
            'stock_name': 'stockName',
            'logo_url': 'logoUrl',
            'amount': 'amount',
            'stock_value': 'stockValue',
            'stock_buyin_price': 'stock_buyin_price'
        }

        self._symbol = symbol
        self._stock_name = stock_name
        self._logo_url = logo_url
        self._amount = amount
        self._stock_value = stock_value
        self._stock_buyin_price = stock_buyin_price

    @classmethod
    def from_dict(cls, dikt) -> 'PortfolioPosition':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PortfolioPosition of this PortfolioPosition.  # noqa: E501
        :rtype: PortfolioPosition
        """
        return util.deserialize_model(dikt, cls)

    @property
    def symbol(self) -> str:
        """Gets the symbol of this PortfolioPosition.


        :return: The symbol of this PortfolioPosition.
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol: str):
        """Sets the symbol of this PortfolioPosition.


        :param symbol: The symbol of this PortfolioPosition.
        :type symbol: str
        """

        self._symbol = symbol

    @property
    def stock_name(self) -> str:
        """Gets the stock_name of this PortfolioPosition.


        :return: The stock_name of this PortfolioPosition.
        :rtype: str
        """
        return self._stock_name

    @stock_name.setter
    def stock_name(self, stock_name: str):
        """Sets the stock_name of this PortfolioPosition.


        :param stock_name: The stock_name of this PortfolioPosition.
        :type stock_name: str
        """

        self._stock_name = stock_name

    @property
    def logo_url(self) -> str:
        """Gets the logo_url of this PortfolioPosition.


        :return: The logo_url of this PortfolioPosition.
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url: str):
        """Sets the logo_url of this PortfolioPosition.


        :param logo_url: The logo_url of this PortfolioPosition.
        :type logo_url: str
        """

        self._logo_url = logo_url

    @property
    def amount(self) -> int:
        """Gets the amount of this PortfolioPosition.


        :return: The amount of this PortfolioPosition.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount: int):
        """Sets the amount of this PortfolioPosition.


        :param amount: The amount of this PortfolioPosition.
        :type amount: int
        """

        self._amount = amount

    @property
    def stock_value(self) -> StockValue:
        """Gets the stock_value of this PortfolioPosition.


        :return: The stock_value of this PortfolioPosition.
        :rtype: StockValue
        """
        return self._stock_value

    @stock_value.setter
    def stock_value(self, stock_value: StockValue):
        """Sets the stock_value of this PortfolioPosition.


        :param stock_value: The stock_value of this PortfolioPosition.
        :type stock_value: StockValue
        """

        self._stock_value = stock_value

    @property
    def stock_buyin_price(self) -> float:
        """Gets the stock_buyin_price of this PortfolioPosition.


        :return: The stock_buyin_price of this PortfolioPosition.
        :rtype: float
        """
        return self._stock_buyin_price

    @stock_buyin_price.setter
    def stock_buyin_price(self, stock_buyin_price: float):
        """Sets the stock_buyin_price of this PortfolioPosition.


        :param stock_buyin_price: The stock_buyin_price of this PortfolioPosition.
        :type stock_buyin_price: float
        """

        self._stock_buyin_price = stock_buyin_price
