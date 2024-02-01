"""Routines to validate Armstrong numbers"""


def is_armstrong_number(number):
    """Validate number has the Armstrong characteristics.

    :param number: int - the number to validate
    :returns: bool - True when characteristics are present, False otherwise
    """

    number_string = str(number)
    number_of_digits = len(number_string)
    armstrong_sum = 0

    for digit in number_string:
        armstrong_sum += int(digit) ** number_of_digits

    if armstrong_sum == number:
        return True

    return False
