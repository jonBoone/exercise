"""Determine reponses Bob will have to given inputs."""


def is_question(message):
    """Determine if input is a question.

    :param input: str - the input to analyze.
    :return: bool - True if input is a question, False otherwise.
    """

    if message[-1] == "?":
        return True

    return False


def is_silence(message):
    """Determine if the input is silence.

    :param input: str - the input to analyze.
    :return: bool - True if empty string, False otherwise.
    """

    if message == '':
        return True

    return False


def is_yelling(message):
    """Determine if the input is being yelled.

    :param input: str - the input to analyze.
    :return: bool - True if input is in ALL_CAPS, False otherwise.
    """

    for letter in message.split():
        if not letter.isupper():
            return False

    return True


def response(hey_bob):
    """Return Bob's response to the input.

    :param hey_bob: str - the input to which Bob must respond.
    :return: str - Bob's response
    """

    # stripping the whitespace converges all relevant silence to ""
    hey_bob = hey_bob.strip()
    if is_silence(hey_bob):
        return "Fine. Be that way!"

    # determine if the input is a question and/or is being yelled
    question = is_question(hey_bob)
    yelled = is_yelling(hey_bob)

    if question and yelled:
        return "Calm down, I know what I'm doing!"

    if question:
        return "Sure."

    if yelled:
        return "Whoa, chill out!"

    return "Whatever."
