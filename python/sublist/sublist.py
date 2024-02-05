"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST: int = 0
SUPERLIST: int = 1
EQUAL: int = 2
UNEQUAL: int = 3


def sublist(list_one, list_two) -> int:

    list_one_length = len(list_one)
    list_two_length = len(list_two)

    if list_one_length == list_two_length:
        # either equal
        pass
    elif list_one_length < list_two_length:
        # sublist
        pass
    else:
        # superlist
        pass

    return UNEQUAL
