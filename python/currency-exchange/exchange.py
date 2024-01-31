"""Functions for calculating steps in exchaning currency.

Python numbers documentation:
https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling:
https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""


def exchange_money(budget, exchange_rate):
    """Calculate the value of the foreign currency received in the exchange.

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """Calculate the redisual budget value after the exchange.

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange.
    :return: float - amount left of your starting currency after exchanging.
    """

    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """Calculate the total value of the exchanged currency.

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """

    return number_of_bills * denomination


def get_number_of_bills(amount, denomination):
    """Calculate the number of bills received in the exchange.

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """

    return amount // denomination


def get_leftover_of_bills(amount, denomination):
    """Calculate the excess currency value kept by the exchange.

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the denomination.
    """

    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """Calculate the maximum value of the currency received in the exchange.

    :param budget: float - the amount of your money you want to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    percent = spread / 100
    adjusted_rate = exchange_rate * (1 + percent)
    target_value = exchange_money(budget, adjusted_rate)
    currentcy_units = get_number_of_bills(target_value, denomination)
    return get_value_of_bills(currentcy_units, denomination)
