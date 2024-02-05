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


def is_sublist(first_list: str, second_list: str) -> bool:
    """determine if second_list is a sublist of first_list

    :param first_list: the reference list
    :type first_list: str
    :param second_list: the list to campare to the reference list
    :type second_list: str
    :return: True, if second_list is a sublist of first_list; False, otherwise
    :rtype: bool
    """
    for i in range(len(first_list) - len(second_list) + 1):
        if not second_list or second_list == first_list[i : i + len(second_list)]:
            return True
    return False


def sublist(list_one: str , list_two: str) -> int:
    """Determine the relationship (SUBLIST, SUPERLIST, EQUAL, UNEQUAL)
    between two provided lists

    :param list_one: the first list to compare
    :type list_one: str
    :param list_two: the second list to compare
    :type list_two: str
    :return: return the relationship of the first list to the second list
    :rtype: int
    """
    list_one_length = len(list_one)
    list_two_length = len(list_two)

    if list_one == list_two:
        return EQUAL
    elif is_sublist(list_one, list_two):
        return SUPERLIST
    elif is_sublist(list_two, list_one):
        return SUBLIST

    return UNEQUAL
