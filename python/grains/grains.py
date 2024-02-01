"""Calculate the number of grains a chessboard holds."""


def square(number):
    """Calculate the number of grains on a specified square.

    :param number: int - a number 1 - 64 indicating which the chosen square
    :return: int - the number of grains on the square

    :raises: ValueError - when number not between 1 and 64
    """

    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")

    return 1 << (number - 1)


def total():
    """Calculate the toal number of grains on a chessboard.

    :return: the total number of grains on a chessboard (64!)
    """

    return (1 << 64) - 1
