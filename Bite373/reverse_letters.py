def reverse_letters(string: str) -> str:
    """Reverse letters in a string but keep the order of the non-letters the same"""

    letters = [letter for letter in string if letter.isalpha()]
    result = []

    for char in string:
        print(char)
        if char.isalpha():
            result.append(letters.pop())
            print(result)
        else:
            result.append(char)

    return "".join(result)


if __name__ == "__main__":
    reverse_letters("ab-cd")
