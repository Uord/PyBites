from collections import Counter

def freq_digit(num: int) -> int:
    counter = Counter(str(num))
    return int(counter.most_common(1)[0][0])
