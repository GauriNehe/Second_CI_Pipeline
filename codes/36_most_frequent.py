from collections import Counter

def most_frequent(lst: list):
    if not lst:
        return None
    return Counter(lst).most_common(1)[0][0]