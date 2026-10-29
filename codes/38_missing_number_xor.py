def find_missing_xor(nums: list) -> int:
    # Finds missing number in range 1 to n (where len(nums) == n - 1)
    n = len(nums) + 1
    xor_all = 0
    xor_nums = 0
    for i in range(1, n + 1):
        xor_all ^= i
    for num in nums:
        xor_nums ^= num
    return xor_all ^ xor_nums