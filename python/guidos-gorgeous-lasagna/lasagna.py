"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

# A Lasagna is expected to bake for 40 minutes
EXPECTED_BAKE_TIME = 40


def bake_time_remaining(elapsed_bake_time) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


# Each lasagna layer takes 2 minutes to prepare
PREPARATION_TIME = 2


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int - the amount of time the lasagna must bake (PREPARTION_TIME * number_of_layers)
    """

    return PREPARATION_TIME * number_of_layers


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total time involved in making the lasagna thus far.

    :param number_of_layers: int - number of layers in the lasgna.
    :param elapsed_bake_time: int - time the lasgna has been baking thus far.
    :return: int - preparation time + elapsed_bake_time
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
