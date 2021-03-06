# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class StockDescription(Model):
    """
    desc: StockDescription contains a number of describing attributes like financials and company size of a certain stock
    author: Luca Mueller
    date: 2020-11-09
    """

    def __init__(self, symbol: str=None, stock_name: str=None, country: str=None, logo_url: str=None, long_description: str=None, industry: str=None, dividend: str=None, market_cap: int=None, fifty_two_week_low: float=None, fifty_two_week_high: float=None, full_time_employees: int=None):  # noqa: E501
        """StockDescription - a model defined in Swagger

        :param symbol: The symbol of this StockDescription.  # noqa: E501
        :type symbol: str
        :param stock_name: The stock_name of this StockDescription.  # noqa: E501
        :type stock_name: str
        :param country: The country of this StockDescription.  # noqa: E501
        :type country: str
        :param logo_url: The logo_url of this StockDescription.  # noqa: E501
        :type logo_url: str
        :param long_description: The long_description of this StockDescription.  # noqa: E501
        :type long_description: str
        :param industry: The industry of this StockDescription.  # noqa: E501
        :type industry: str
        :param dividend: The dividend of this StockDescription.  # noqa: E501
        :type dividend: str
        :param market_cap: The market_cap of this StockDescription.  # noqa: E501
        :type market_cap: int
        :param fifty_two_week_low: The fifty_two_week_low of this StockDescription.  # noqa: E501
        :type fifty_two_week_low: float
        :param fifty_two_week_high: The fifty_two_week_high of this StockDescription.  # noqa: E501
        :type fifty_two_week_high: float
        :param full_time_employees: The full_time_employees of this StockDescription.  # noqa: E501
        :type full_time_employees: int
        """
        self.swagger_types = {
            'symbol': str,
            'stock_name': str,
            'country': str,
            'logo_url': str,
            'long_description': str,
            'industry': str,
            'dividend': str,
            'market_cap': int,
            'fifty_two_week_low': float,
            'fifty_two_week_high': float,
            'full_time_employees': int
        }

        self.attribute_map = {
            'symbol': 'symbol',
            'stock_name': 'stockName',
            'country': 'country',
            'logo_url': 'logoUrl',
            'long_description': 'longDescription',
            'industry': 'industry',
            'dividend': 'dividend',
            'market_cap': 'marketCap',
            'fifty_two_week_low': 'fiftyTwoWeekLow',
            'fifty_two_week_high': 'fiftyTwoWeekHigh',
            'full_time_employees': 'fullTimeEmployees'
        }

        self._symbol = symbol
        self._stock_name = stock_name
        self._country = country
        self._logo_url = logo_url
        self._long_description = long_description
        self._industry = industry
        self._dividend = dividend
        self._market_cap = market_cap
        self._fifty_two_week_low = fifty_two_week_low
        self._fifty_two_week_high = fifty_two_week_high
        self._full_time_employees = full_time_employees

    @classmethod
    def from_dict(cls, dikt) -> 'StockDescription':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The StockDescription of this StockDescription.  # noqa: E501
        :rtype: StockDescription
        """
        return util.deserialize_model(dikt, cls)

    @property
    def symbol(self) -> str:
        """Gets the symbol of this StockDescription.


        :return: The symbol of this StockDescription.
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol: str):
        """Sets the symbol of this StockDescription.


        :param symbol: The symbol of this StockDescription.
        :type symbol: str
        """

        self._symbol = symbol

    @property
    def stock_name(self) -> str:
        """Gets the stock_name of this StockDescription.


        :return: The stock_name of this StockDescription.
        :rtype: str
        """
        return self._stock_name

    @stock_name.setter
    def stock_name(self, stock_name: str):
        """Sets the stock_name of this StockDescription.


        :param stock_name: The stock_name of this StockDescription.
        :type stock_name: str
        """

        self._stock_name = stock_name

    @property
    def country(self) -> str:
        """Gets the country of this StockDescription.


        :return: The country of this StockDescription.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country: str):
        """Sets the country of this StockDescription.


        :param country: The country of this StockDescription.
        :type country: str
        """

        self._country = country

    @property
    def logo_url(self) -> str:
        """Gets the logo_url of this StockDescription.


        :return: The logo_url of this StockDescription.
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url: str):
        """Sets the logo_url of this StockDescription.


        :param logo_url: The logo_url of this StockDescription.
        :type logo_url: str
        """

        self._logo_url = logo_url

    @property
    def long_description(self) -> str:
        """Gets the long_description of this StockDescription.


        :return: The long_description of this StockDescription.
        :rtype: str
        """
        return self._long_description

    @long_description.setter
    def long_description(self, long_description: str):
        """Sets the long_description of this StockDescription.


        :param long_description: The long_description of this StockDescription.
        :type long_description: str
        """

        self._long_description = long_description

    @property
    def industry(self) -> str:
        """Gets the industry of this StockDescription.


        :return: The industry of this StockDescription.
        :rtype: str
        """
        return self._industry

    @industry.setter
    def industry(self, industry: str):
        """Sets the industry of this StockDescription.


        :param industry: The industry of this StockDescription.
        :type industry: str
        """

        self._industry = industry

    @property
    def dividend(self) -> str:
        """Gets the dividend of this StockDescription.


        :return: The dividend of this StockDescription.
        :rtype: str
        """
        return self._dividend

    @dividend.setter
    def dividend(self, dividend: str):
        """Sets the dividend of this StockDescription.


        :param dividend: The dividend of this StockDescription.
        :type dividend: str
        """

        self._dividend = dividend

    @property
    def market_cap(self) -> int:
        """Gets the market_cap of this StockDescription.


        :return: The market_cap of this StockDescription.
        :rtype: int
        """
        return self._market_cap

    @market_cap.setter
    def market_cap(self, market_cap: int):
        """Sets the market_cap of this StockDescription.


        :param market_cap: The market_cap of this StockDescription.
        :type market_cap: int
        """

        self._market_cap = market_cap

    @property
    def fifty_two_week_low(self) -> float:
        """Gets the fifty_two_week_low of this StockDescription.


        :return: The fifty_two_week_low of this StockDescription.
        :rtype: float
        """
        return self._fifty_two_week_low

    @fifty_two_week_low.setter
    def fifty_two_week_low(self, fifty_two_week_low: float):
        """Sets the fifty_two_week_low of this StockDescription.


        :param fifty_two_week_low: The fifty_two_week_low of this StockDescription.
        :type fifty_two_week_low: float
        """

        self._fifty_two_week_low = fifty_two_week_low

    @property
    def fifty_two_week_high(self) -> float:
        """Gets the fifty_two_week_high of this StockDescription.


        :return: The fifty_two_week_high of this StockDescription.
        :rtype: float
        """
        return self._fifty_two_week_high

    @fifty_two_week_high.setter
    def fifty_two_week_high(self, fifty_two_week_high: float):
        """Sets the fifty_two_week_high of this StockDescription.


        :param fifty_two_week_high: The fifty_two_week_high of this StockDescription.
        :type fifty_two_week_high: float
        """

        self._fifty_two_week_high = fifty_two_week_high

    @property
    def full_time_employees(self) -> int:
        """Gets the full_time_employees of this StockDescription.


        :return: The full_time_employees of this StockDescription.
        :rtype: int
        """
        return self._full_time_employees

    @full_time_employees.setter
    def full_time_employees(self, full_time_employees: int):
        """Sets the full_time_employees of this StockDescription.


        :param full_time_employees: The full_time_employees of this StockDescription.
        :type full_time_employees: int
        """

        self._full_time_employees = full_time_employees
