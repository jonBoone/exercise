"""Provide tools to determine the type of triangle (equilateral, isosceles,
scalene)."""


def triangle_inequality(sides):
    """Validate triangle inequalities hold for sides

    :param sides: list - the lengths of the three sides
    :return: bool - return True if all inequalities hold, otherwise False
    """

    (a, b, c) = sides

    if a + b < c:
        return False

    if b + c < a:
        return False

    if a + c < b:
        return False

    return True


def non_zero_sides(sides):
    """Validate all three sides are non-zero

    :param sides: list - the lengths of the three sides
    :return: bool - if all sides > 0 return True, otherwise False
    """

    if sides[0] <= 0:
        return False

    if sides[1] <= 0:
        return False

    if sides[2] <= 0:
        return False

    return True


def triangle(sides):
    """Validate we have an actual triangle

    :param sides: list - the lengths of the three sides
    :return: bool - return True if an actual triange, otherwise False
    """

    if triangle_inequality(sides) and non_zero_sides(sides):
        return True

    return False


def same_length(sides):
    """Verify sides are the same length

    :param sides: list - the lengths of the three sides
    :return: bool - return True if sides are all equal, otherwise False
    """

    if sides[0] == sides[1] == sides[2]:
        return True

    return False


def equilateral(sides):
    """Return True if triangle is equilateral; otheriwse False

    :param sides: list -  the lengths of the three sides
    :return: bool - return True if all sides are equal; otherwise False
    """

    if triangle(sides) and same_length(sides):
        return True

    return False


def isosceles(sides):
    pass


def scalene(sides):
    pass
