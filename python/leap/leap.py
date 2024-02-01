"""Validate leap years"""


def leap_year(year):
    """Validate a given year is a leap year

    :param year: int - a specific year in the Gregorian calendar
    :return: bool - return True if year is a leap year, False otherwise
    """

    divisible_by_four = year % 4 == 0
    divisible_by_hundred = year % 100 == 0
    divisible_by_four_hundred = year % 400 == 0

    if divisible_by_four_hundred:
        return True

    if divisible_by_hundred:
        return False

    if divisible_by_four:
        return True

    return False
