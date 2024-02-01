"""Calculate the number of grains a chessboard holds."""


def square(number):
    """Calculate the number of grains on a specified square.

    :param number: int - a number 1 - 64 indicating which the chosen square
    :return: int - the number of grains on the square
    """

    return 2**(number - 1)


def total():
    pass
