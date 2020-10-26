# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class PortfolioPosition(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, symbol: str=None, logo_url: str=None, stock_name: str=None, amount: int=None, stock_price: float=None, stock_buyin_price: float=None, country_id: str=None, industry: str=None):  # noqa: E501
        """PortfolioPosition - a model defined in Swagger

        :param symbol: The symbol of this PortfolioPosition.  # noqa: E501
        :type symbol: str
        :param logo_url: The logo_url of this PortfolioPosition.  # noqa: E501
        :type logo_url: str
        :param stock_name: The stock_name of this PortfolioPosition.  # noqa: E501
        :type stock_name: str
        :param amount: The amount of this PortfolioPosition.  # noqa: E501
        :type amount: int
        :param stock_price: The stock_price of this PortfolioPosition.  # noqa: E501
        :type stock_price: float
        :param stock_buyin_price: The stock_buyin_price of this PortfolioPosition.  # noqa: E501
        :type stock_buyin_price: float
        :param country_id: The country_id of this PortfolioPosition.  # noqa: E501
        :type country_id: str
        :param industry: The industry of this PortfolioPosition.  # noqa: E501
        :type industry: str
        """
        self.swagger_types = {
            'symbol': str,
            'logo_url': str,
            'stock_name': str,
            'amount': int,
            'stock_price': float,
            'stock_buyin_price': float,
            'country_id': str,
            'industry': str
        }

        self.attribute_map = {
            'symbol': 'symbol',
            'logo_url': 'logoUrl',
            'stock_name': 'stockName',
            'amount': 'amount',
            'stock_price': 'stock_price',
            'stock_buyin_price': 'stock_buyin_price',
            'country_id': 'countryId',
            'industry': 'industry'
        }

        self._symbol = symbol
        self._logo_url = logo_url
        self._stock_name = stock_name
        self._amount = amount
        self._stock_price = stock_price
        self._stock_buyin_price = stock_buyin_price
        self._country_id = country_id
        self._industry = industry

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
    def stock_price(self) -> float:
        """Gets the stock_price of this PortfolioPosition.


        :return: The stock_price of this PortfolioPosition.
        :rtype: float
        """
        return self._stock_price

    @stock_price.setter
    def stock_price(self, stock_price: float):
        """Sets the stock_price of this PortfolioPosition.


        :param stock_price: The stock_price of this PortfolioPosition.
        :type stock_price: float
        """

        self._stock_price = stock_price

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

    @property
    def country_id(self) -> str:
        """Gets the country_id of this PortfolioPosition.


        :return: The country_id of this PortfolioPosition.
        :rtype: str
        """
        return self._country_id

    @country_id.setter
    def country_id(self, country_id: str):
        """Sets the country_id of this PortfolioPosition.


        :param country_id: The country_id of this PortfolioPosition.
        :type country_id: str
        """

        self._country_id = country_id

    @property
    def industry(self) -> str:
        """Gets the industry of this PortfolioPosition.


        :return: The industry of this PortfolioPosition.
        :rtype: str
        """
        return self._industry

    @industry.setter
    def industry(self, industry: str):
        """Sets the industry of this PortfolioPosition.


        :param industry: The industry of this PortfolioPosition.
        :type industry: str
        """

        self._industry = industry
