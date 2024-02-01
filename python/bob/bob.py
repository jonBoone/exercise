"""Determine reponses Bob will have to given inputs."""


def is_question(input):
    """Determine if input is a question.

    :param input: str - the input to analyze.
    :return: bool - True if input is a question, False otherwise.
    """

    if input[-1] == "?":
        return True

    return False


def response(hey_bob):
    """Return Bob's response to the input.

    :param hey_bob: str - the input to which Bob must respond.
    :return: str - Bob's response
    """

    if is_question(hey_bob):
        return "Sure."

    return "Whatever."
