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


def compare_lists(list_one: str, list_two: str, 
                  comparison_length: int) -> bool:
    """Given two lists, determine if they are identical across a given
    number of elements

    :param list_one: the first list to compare
    :type list_one: str
    :param list_two: the second list to compare
    :type list_two: str
    :param comparison_length: the number of elements that nmust be equal
    :type comparison_length: int
    :return: True if the first comparison_length elements in both lists are the same, False otherwise
    :rtype: bool
    """
    return False

def sublist(list_one:str , list_two: str) -> int:
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

    if list_one_length == list_two_length and \
    compare_lists(list_one, list_two, list_one_length):
        return EQUAL
    elif list_one_length < list_two_length:
        for index in range(list_two_length - list_one_length):
            if compare_lists(list_one, 
                             list_two[index:index + list_one_length], 
                             list_one_length):
                return SUBLIST
    else:
        for index in range(list_one_length - list_two_length):
            if compare_lists(list_one[index:index + list_two_length],
                             list_two,
                             list_two_length):
                return SUPERLIST

    return UNEQUAL
