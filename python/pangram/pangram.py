"""Pangram validation functionality"""
def is_pangram(sentence:str):
    """validate that sentence is a pangram of the English letters

    :param sentence: the text to validate
    :type sentence: str
    :return: True when text contains all English letters, False otherwise
    :rtype: _type_
    """
    english_alphabet: list[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                                   'h', 'i', 'j', 'k', 'l', 'm', 'n',
                                   'o', 'p', 'q', 'r', 's', 't', 'u',
                                   'v', 'w', 'x', 'y', 'z']

    letters_used: dict = { key: 0 for key in english_alphabet}

    for component in sentence:
        if component.isalpha():
            key: str = component.lower()
            letters_used[key] += 1

    unused_letters: list[str] = [ key for key in letters_used.keys()
                                  if letters_used[key] == 0 ]


    if len(unused_letters) == 0:
        return True

    return False
