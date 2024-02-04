

latin_alphabet: list[str] = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                                  'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                                  's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]


def generate_cipher(key: int) -> dict:
    """Generate a rotatinoal cipher using base lowecase latin alphabet.

    :param key: the number of places by which to rotate the latin alphabet
    :type key: int
    :return: the cipher alphabet
    :rtype: dict
    """
    
    return {value: (index + key) % len(latin_alphabet) for index, value in enumerate(latin_alphabet)}



def process_letter(letter: str, cipher: dict) -> str:
    """Perform the appropriate substitution for the element provided.

    :param letter: element of the text to substitute
    :type letter: str
    :param cipher: replacement alphabet
    :type cipher: dict
    :return: the substitution performed for the given element
    :rtype: str
    """
    upcaseResult: bool = False
    result: str = ''

    if letter.isalpha():
        if letter.isupper():
            upcaseResult = True
            letter = letter.lower()
        result_index = cipher[letter]
        result = latin_alphabet[result_index]
        if upcaseResult:
            result = result.upper()
        return result

    return letter


def rotate(text: str, key: int) -> str:
    cipher = generate_cipher(key)
    result_text: list[str] = ''

    for letter in text:
        result_text = result_text + process_letter(letter, cipher)

    return result_text
