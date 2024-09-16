import string

def validate_pangram(sentence: str) -> bool:
    """Check if a sentence is a pangram
    A pangram is a sentence containing every letter in the English alphabet.
    The input `sentence` should be a string containing only English letters.
    The function returns True if the sentence is a pangram, and False otherwise.
    """

    alphabet_string = string.ascii_lowercase
    return set(alphabet_string) == set(char for char in sentence.lower() if char.isalpha())
    


if __name__ == "__main__":
    validate_pangram()