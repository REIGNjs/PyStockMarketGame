import connexion
import six

from swagger_server.models.api_error import ApiError  # noqa: E501
from swagger_server.models.portfolio_position import PortfolioPosition  # noqa: E501
from swagger_server.models.portfolio_value import PortfolioValue  # noqa: E501
from swagger_server.models.transaction import Transaction  # noqa: E501
from swagger_server.models.transaction_prepare import TransactionPrepare  # noqa: E501
from swagger_server import util


def create_transaction(transaction_prepare_param):  # noqa: E501
    """Create a new stock transaction

    Creates and executes a transaction for the logged in user # noqa: E501

    :param transaction_prepare_param: The transaction to create.
    :type transaction_prepare_param: dict | bytes

    :rtype: Transaction
    """
    if connexion.request.is_json:
        transaction_prepare_param = TransactionPrepare.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_portfolio():  # noqa: E501
    """Get all current positions

    Returns all the current stock positions of the logged in user # noqa: E501


    :rtype: List[PortfolioPosition]
    """
    return 'do some magic!'


def get_portfolio_value():  # noqa: E501
    """Get the performance of the portfolio

    Returns the logged in users portfolio performance # noqa: E501


    :rtype: List[PortfolioValue]
    """
    return 'do some magic!'
