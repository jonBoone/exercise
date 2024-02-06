"""Classify numbers according to it's aliquot sum."""


def aliquot_sum(number: int) -> int:
    """Calculate the aliquot sum of the given number.

    :param number: the number of which to calculate the sum of it's factors
    :type number: int
    :return: the sum of all factors of the number excluding itself
    :rtype: int
    """
    pass

def classify(number: int) -> str:
    """ A perfect number equals the sum of its positive divisors.

    :param number: the number to classify
    :type number: int
    :return: the classification of the input integer
    :rtype: str
    """

    aliquot: int = aliquot_sum(number)
    if aliquot < number:
        return 'deficient'

    if aliquot > number:
        return 'abundant'

    return 'perfect'
