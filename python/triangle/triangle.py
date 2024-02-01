"""Provide tools to determine the type of triangle (equilateral, isosceles,
scalene)."""


def equilateral(sides):
    """Return True if triangle is equilateral; otheriwse False

    :param sides: list -  the lengths of the three sides
    :return: bool - return True if all sides are equal; otherwise False
    """

    if sides[0] == sides[1] == sides[2]:
        return True

    return False


def isosceles(sides):
    pass


def scalene(sides):
    pass
