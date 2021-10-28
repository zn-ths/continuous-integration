VOWELS = ["a", "e", "i", "o", "u", "y"]


def remove_vowels(word: str) -> str:
    """Returns a string without any vowels: aeiouy.

    Args:
        word (str): the string to remove vowels from.
    Returns:
        str: string without any vowels.
    """

    return "".join([letter for letter in word if letter.lower() not in VOWELS])


def reverse_string(word: str) -> str:
    """Returns a reversed string.

    Args:
        word (str): the string to reverse.
    Returns:
        str: the reversed string.
    """

    return word[::-1]


def main():
    print(remove_vowels("zaid"))
    print(remove_vowels("Anna babbah alsO"))
    print(reverse_string("zaid"))
    print(reverse_string("annA bAbbah alsO"))


if __name__ == "__main__":
    main()
