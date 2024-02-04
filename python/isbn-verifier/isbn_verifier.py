"""Validate ISBN-10 Numbers"""
def is_valid(isbn: str) -> bool:
    """Verify the given string represents a valid ISBN-10 number.

    :param isbn: a presumed ISBN-10 number
    :type isbn: str
    :return: True when isbn validates properly, False otherwise
    :rtype: bool
    """

    isbn_sans_formatting:str = isbn.replace('-', '')

    if len(isbn_sans_formatting) != 10:
        return False

    sum = 0

    for i in range(10, 0, -1):
        digit_value = isbn_sans_formatting[-i]
        if digit_value.isalpha():
            if digit_value == 'X' and i == 1:
                digit_value = '10'
            else:
                return False
        sum += int(digit_value) * i

    if sum % 11 != 0:
        return False

    return True
