"""Provide Pig Latin functionality."""


vowel_sounds = ('xr', 'yt')
vowels = ('a','e','i','o','u')


def begins_with_vowel_sound(word):
    """Validate the given English word begins with a vowel sound.

    :param word: str - the English word to check
    :result: str - True, when word begins with a vowel cluster, False otherwise
    """

    if word[:2] in vowel_sounds:
        return True

    beginning_vowel_cluster = ''

    for component in word:
        if component in vowels:
            beginning_vowel_cluster += component
        else:
            break

    if '' != beginning_vowel_cluster:
        return True

    return False


def add_ay_to_end(word):
    """Add 'ay' sound to the end of the word.

    :param text: str - word beginning with a vowel sound.
    :return: str - the word with an 'ay' suffix added
    """

    return word + 'ay'


def translate(text):
    """Translate a provided English text into Pig Latin.

    :param text: str - the source English phrase.
    :return: str - the translated Pig Latin phrase.
    """
    pass