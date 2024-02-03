"""Functionality to validate apparent isograms
"""


def is_isogram(string: str) -> bool:
    """validate if the phrase is an isogram

    :param string: the phrase to validate
    :type string: str
    :return: True if isogram, False otherwise
    :rtype: bool
    """
    components: dict = {}

    for component in string:  # type: str
        component = component.lower() # type: str
        if component in components.keys():  # type: bool
            if component.isalpha():  # type: bool
                return False  #rtype: bool

        components[component] = True # type: bool

    return True  # rtype: bool
