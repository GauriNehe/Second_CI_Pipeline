from collections import Counter

def first_non_repeating(s: str):
    counts = Counter(s)
    for char in s:
        if counts[char] == 1:
            return char
    return None