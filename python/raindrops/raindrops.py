"""Increased Complexity Version of FizzBuzz)"""


def convert(number):
    """Convert intenger to corresponding raindrop sound.

    :param number: int - the integer to convert
    :return: str - the raindrop sounds corresponding to the number
    """
    divisible_by_three = number % 3 == 0
    divisible_by_five = number % 5 == 0
    divisible_by_seven = number % 7 == 0
    found_divisor = False

    raindrop_sounds = ''

    if divisible_by_three:
        raindrop_sounds += 'Pling'
        found_divisor = True

    if divisible_by_five:
        raindrop_sounds += 'Plang'
        found_divisor = True

    if divisible_by_seven:
        raindrop_sounds += 'Plong'
        found_divisor = True

    if not found_divisor:
        raindrop_sounds = str(number)

    return raindrop_sounds
