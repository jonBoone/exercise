


def generate_cipher(key: int) -> dict:
    """Generate a rotatinoal cipher using base lowecase latin alphabet.

    :param key: the number of places by which to rotate the latin alphabet
    :type key: int
    :return: the cipher alphabet
    :rtype: dict
    """
    latin_alphabet: list[str] = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                                  'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                                  's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
    
    return {value: (index + key) % len(latin_alphabet) for index, value in enumerate(latin_alphabet)}


def rotate(text: str, key: int) -> str:
    cipher = generate_cipher(key)
    print(f'cipher == {cipher}')