VOWELS = ["a", "e", "i", "o", "u", "y"]


def remove_vowels(word: str) -> str:
    return "".join([letter for letter in word if letter.lower() not in VOWELS])


def reverse_string(word: str) -> str:
    return word[::-1]


def main():
    print(remove_vowels("zaid"))
    print(remove_vowels("Anna babbah alsO"))
    print(reverse_string("zaid"))
    print(reverse_string("annA bAbbah alsO"))


if __name__ == "__main__":
    main()
