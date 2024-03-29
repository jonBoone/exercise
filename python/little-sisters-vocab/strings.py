"""Functions for creating, transforming, and adding prefixes to strings."""

UN_PREFIX = "un"
NESS_SUFFIX = "ness"


def add_prefix(prefix, word) -> str:
    """Take the given word and add the prefix to it.

    :param prefix: str - the prefix of the new string.
    :param word: str - the root word.
    :return: str - prefix + root word.
    """
    return prefix + word


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    return add_prefix(UN_PREFIX, word)


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string beginning
    with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """

    seperator = " :: "
    prefix = vocab_words[0]
    words = vocab_words[1:]
    result = prefix

    for word in words:
        result = result + seperator + add_prefix(prefix, word)

    return result


def remove_suffix(suffix, word):
    """Remove suffix from the word while keeping spelling in mind.

    :param suffix: str - the suffix to remove.
    :param word: str - the target from which to remove the suffix.
    :return: str - word with removed suffix and adjusted spelling.
    """

    root = word[:-(len(suffix))]

    if root[-1] == "i":
        return root[:-1] + "y"

    return root


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    return remove_suffix(NESS_SUFFIX, word)


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """

    words = sentence.split()
    adjective = words[index]

    if adjective[-1] == ".":
        adjective = adjective[:-1]

    return adjective + "en"
