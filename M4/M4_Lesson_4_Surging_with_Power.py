"""
M4 Lesson 4 – Surging with Power!!

Working with powers of 2, highest/lowest set bits, etc.
"""

# Activity 1: Check power of 2 (optimized)
def is_power_of_two(n):
    return n > 0 and (n & (n-1)) == 0

print("=== Surging with Power!! ===")
print("Activity 1: Power of Two Checks")
nums = [1, 2, 3, 4, 8, 16, 31]
for num in nums:
    print(f"{num} -> Power of 2: {is_power_of_two(num)}")

# Activity 2: Find next power of 2
import math
def next_power_of_two(n):
    if n == 0:
        return 1
    n -= 1
    n |= n >> 1
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    n |= n >> 16
    return n + 1

print("\nActivity 2: Next Power of 2")
print("Next power of 2 after 13 is", next_power_of_two(13))

# Activity 3: Count trailing zeros (using bit operations)
def count_trailing_zeros(n):
    if n == 0:
        return 32  # assuming 32-bit
    count = 0
    while (n & 1) == 0:
        count += 1
        n >>= 1
    return count

print("\nActivity 3: Trailing Zeros")
print("Trailing zeros in 24 (11000):", count_trailing_zeros(24))
