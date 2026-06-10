"""
M4 Lesson 5 – Bitplay 3

Advanced Bit Manipulation: XOR tricks, unique number, etc.
"""

# Activity 1: Find single number in array where others appear twice (XOR trick)
def single_number(nums):
    """All elements appear twice except one"""
    res = 0
    for num in nums:
        res ^= num
    return res

print("=== Bitplay 3 ===")
print("Activity 1: Single Number")
arr = [4, 1, 2, 1, 2]
print("Single number in", arr, "is", single_number(arr))

# Activity 2: Find two unique numbers
def two_unique_numbers(nums):
    """Find two numbers that appear once, others twice"""
    xor_all = 0
    for num in nums:
        xor_all ^= num
    
    # Find rightmost set bit
    rightmost = xor_all & -xor_all
    
    num1 = num2 = 0
    for num in nums:
        if num & rightmost:
            num1 ^= num
        else:
            num2 ^= num
    return num1, num2

print("\nActivity 2: Two Unique Numbers")
arr2 = [2, 4, 6, 8, 10, 2, 6, 10]
print("Two unique numbers:", two_unique_numbers(arr2))

# Activity 3: Swap all odd and even bits
def swap_odd_even_bits(n):
    """Swap odd and even positioned bits"""
    even_bits = (n & 0xAAAAAAAA) >> 1   # 1010... 
    odd_bits = (n & 0x55555555) << 1    # 0101...
    return even_bits | odd_bits

print("\nActivity 3: Swap Odd/Even Bits")
n = 23  # 10111
print(f"Original: {n} ({bin(n)})")
print(f"After swap: {swap_odd_even_bits(n)} ({bin(swap_odd_even_bits(n))})")
