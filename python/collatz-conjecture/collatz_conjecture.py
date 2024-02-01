"""Implementation of the Collatz Conjecture Algorithm"""


def is_even(number: int) -> bool:
    """If number is even, return True; otherwise return False

    :param number: int - the potential even number
    :return: bool - True if number is even, else False
    """

    return number % 2 == 0


def even(number: int, step_num: int) -> int:
    """Implementation of the step when the prior value was even

    :param number: int - the number to use for this step
    :param step_num: int - a counter of the number of steps so far
    :return: int - the number of steps completed
    """

    half = number // 2
    step_num += 1

    if half == 1:
        return step_num

    if is_even(half):
        return even(half, step_num)

    return odd(half, step_num)


def odd(number: int, step_num: int) -> int:
    """Implementation of the step when the prior value was odd

    :param number: int - the number to use for this step
    :param step_num: int - a counter of the number of steps so far
    :return: int - the number of steps completed
    """

    three_n_plus_one = (3 * number) + 1
    step_num += 1

    if is_even(three_n_plus_one):
        return even(three_n_plus_one, step_num)

    return odd(three_n_plus_one, step_num)


def steps(number: int) -> int:
    """Implementation of the steps in the algorithm

    :param number: int - Initial number to start from
    :return: int - the number of steps required to reach 1
    """

    step = 0

    if number < 1:
        raise ValueError('Only positive integers are allowed')

    if number == 1:
        return step

    if is_even(number):
        return even(number, step)

    return odd(number, step)
