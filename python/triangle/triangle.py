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


def equilateral(sides):
    """Return True if triangle is equilateral; otheriwse False

    :param sides: list -  the lengths of the three sides
    :return: bool - return True if all sides are equal; otherwise False
    """

    if not non_zero_sides(sides):
        return False

    if sides[0] == sides[1] == sides[2]:
        return True

    return False


def isosceles(sides):
    pass


def scalene(sides):
    pass
