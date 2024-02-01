"""Calculate the number of grains a chessboard holds."""


def factorial_helper(number, result):
    """Calculate the factorial of a given number.

    :param number: int - the particular factorial to compute
    :param result: int - an accumulator of the running total
    :return: int - the result when number == 0
    """

    if result == 0:
        result = 1

    if number == 0:
        return result

    return factorial_helper(number - 1, result * number)


def factorial(number):
    """Calculate factorial using standard math API.

    :param number: int - the factorial to calculate
    :return: int - the factorial of number
    """

    return factorial_helper(number, 0)


def square(number):
    """Calculate the number of grains on a specified square.

    :param number: int - a number 1 - 64 indicating which the chosen square
    :return: int - the number of grains on the square
    """

    return 2**(number - 1)


def total():
    pass
