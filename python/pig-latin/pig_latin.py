"""Provide Pig Latin functionality."""


vowel_sounds = ('xr', 'yt')
vowels = ('a', 'e', 'i', 'o', 'u')
consonant_cluster_vowels = ('u', 'y')


def add_ay_to_end(word):
    """Add 'ay' sound to the end of the word.

    :param text: str - word beginning with a vowel sound.
    :return: str - the word with an 'ay' suffix added
    """

    return word + 'ay'


def begins_with_vowel_sound(word):
    """Validate the given English word begins with a vowel sound.

    :param word: str - the English word to check
    :result: bool - True, when word begins with a vowel cluster, else False
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


def relocate_beginning_consonants(word):
    """Move the beginning consonts to the end of the word.

    :param word: str - the English word to modify.
    :result: str - the modified English word.
    """

    beginning_consonant_cluster = ''

    for component in word:
        if component not in vowels:
            beginning_consonant_cluster += component
        elif component in consonant_cluster_vowels:
            match component:
                case 'y':
                    beginning_consonant_cluster += component
                case 'u':
                    print(f'word == {word}')
                    print(f'beginning_consonant_cluster[-1] = {beginning_consonant_cluster[-1]}')
                    if beginning_consonant_cluster[-1] == 'q':
                        beginning_consonant_cluster += component
                    else:
                        break
        else:
            break

    return word[len(beginning_consonant_cluster):] + \
        word[:len(beginning_consonant_cluster)]


def translate(text):
    """Translate a provided English text into Pig Latin.

    :param text: str - the source English phrase.
    :return: str - the translated Pig Latin phrase.
    """

    translated_text = ''

    text = text.strip()
    text = text.split()

    for index, word in enumerate(text):
        if begins_with_vowel_sound(word):
            translated_text += add_ay_to_end(word)
        if not begins_with_vowel_sound(word):
            translated_word = relocate_beginning_consonants(word)
            translated_text += add_ay_to_end(translated_word)
        if index != len(text) - 1:
            translated_text += ' '

    return translated_text
