"""Classify numbers according to it's aliquot sum."""

import math

def aliquot_sum(number: int) -> int:
    """Calculate the aliquot sum of the given number.

    :param number: the number of which to calculate the sum of it's factors
    :type number: int
    :return: the sum of all factors of the number excluding itself
    :rtype: int
    """

    factors = set()

    for item in range(1, math.isqrt(number)+ 1):
        if number % item != 0:
            continue
        factors.add(item)
        factors.add(number // item)

    factors.remove(number)
    aliquot: int = sum(factors)
    return aliquot


def classify(number: int) -> str:
    """ A perfect number equals the sum of its positive divisors.

    :param number: the number to classify
    :type number: int
    :return: the classification of the input integer
    :rtype: str
    """

    if not (type(number) == int and number > 0):
        raise ValueError('Classification is only possible for positive integers.')

    aliquot: int = aliquot_sum(number)

    if aliquot < number:
        return 'deficient'

    if aliquot > number:
        return 'abundant'

    return 'perfect'
