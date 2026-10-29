def is_pangram(s: str) -> bool:
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return alphabet.issubset(set(s.lower()))