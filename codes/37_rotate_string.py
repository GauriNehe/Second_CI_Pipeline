def rotate_string(s: str, k: int) -> str:
    if not s:
        return s
    k = k % len(s)
    return s[k:] + s[:k]
