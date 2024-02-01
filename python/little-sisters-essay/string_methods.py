"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title):
    """Ensure the first letter of each word in the title is uppercase.

    :param title: str - title string that needs title casing.
    :return: str - title string in title case (first letters capitalized).
    """

    words = title.split()
    return " ".join([word.capitalize() for word in words])


def check_sentence_ending(sentence):
    """Check the ending of the sentence to verify that a period is present.

    :param sentence: str - a sentence to check.
    :return: bool - return True if correctly punctuated, False otherwise.
    """

    pass


def clean_up_spacing(sentence):
    """Remove any whitespace at the start and end of the sentence.

    :param sentence: str - a sentence from which to clean up whitespace.
    :return: str - a cleaned up sentence with no leading/trailing whitespace.
    """

    pass


def replace_word_choice(sentence, old_word, new_word):
    """Replace a word in the provided sentence with a new one.

    :param sentence: str - a sentence to replace words in.
    :param old_word: str - word to replace.
    :param new_word: str - replacement word.
    :return: str - input sentence with new words in place of old words.
    """

    pass
