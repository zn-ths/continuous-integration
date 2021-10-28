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


def convert_to_robbers_lang(text: str) -> str:
    """Returns a modified string converted to robbers language.

    Replaces all consonants with duplicates of the consonant with
    an 'o' in between.

    Args:
        text (str): the string to modify.
    Returns:
        str: the string converted to robbers language.
    """

    is_consonant = lambda char: char.lower() not in VOWELS and char.isalpha()
    return "".join([f"{c}o{c}" if is_consonant(c) else c for c in text])


def main():
    print(remove_vowels("zaid"))
    print(remove_vowels("Anna babbah alsO"))
    print(reverse_string("zaid"))
    print(reverse_string("annA bAbbah alsO"))
    print(convert_to_robbers_lang("zaiD"))


if __name__ == "__main__":
    main()
