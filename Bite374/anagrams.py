def group_anagrams(strings: list[str]) -> list[list[str]]:
    """Group anagrams together."""

    anagrams = {}

    for word in strings:
        sorted_word = "".join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]

    return list(anagrams.values())


if __name__ == "__main__":
    group_anagrams()
