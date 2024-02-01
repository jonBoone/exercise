"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title):
    """Ensure the first letter of each word in the title is uppercase.

    :param title: str - title string that needs title casing.
    :return: str - title string in title case (first letters capitalized).
    """

    return title.title()


def check_sentence_ending(sentence):
    """Check the ending of the sentence to verify that a period is present.

    :param sentence: str - a sentence to check.
    :return: bool - return True if correctly punctuated, False otherwise.
    """

    return sentence.endswith('.')


def clean_up_spacing(sentence):
    """Remove any whitespace at the start and end of the sentence.

    :param sentence: str - a sentence from which to clean up whitespace.
    :return: str - a cleaned up sentence with no leading/trailing whitespace.
    """

    return sentence.strip()


def replace_word_choice(sentence, old_word, new_word):
    """Replace a word in the provided sentence with a new one.

    :param sentence: str - a sentence to replace words in.
    :param old_word: str - word to replace.
    :param new_word: str - replacement word.
    :return: str - input sentence with new words in place of old words.
    """

    # Assuming setence parameter contains only a single sentence.
    new_sentence = ''
    ending_punctation = sentence[-1]

    # Ensure that the replacement happens only on entire words,
    # and not on substrings of words that happen to match.
    words = sentence.split()
    words = [word.rstrip(ending_punctation) for word in words]
    final_word = len(words) - 1

    for index, word in enumerate(words):
        if word == old_word:
            new_sentence += new_word
        else:
            new_sentence += word

        if index == final_word:
            new_sentence += ending_punctation
        else:
            new_sentence += ' '

    return new_sentence
