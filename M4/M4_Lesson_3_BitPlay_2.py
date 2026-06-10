"""
M4 Lesson 3 – BitPlay 2

More bit tricks: Count set bits efficiently, Find rightmost set bit, etc.
"""

# Brian Kernighan's Algorithm - Fast way to count set bits
def count_set_bits_fast(n):
    count = 0
    while n:
        n = n & (n - 1)  # Removes the rightmost set bit
        count += 1
    return count

print("=== BitPlay 2 ===")

# Activity 1: Compare counting methods
print("Activity 1: Set Bits Count")
num = 29  # 11101
print(f"Number: {num} ({bin(num)})")
print("Simple method:", bin(num).count('1'))
print("Fast method:", count_set_bits_fast(num))

# Activity 2: Find rightmost set bit position
def rightmost_set_bit_pos(n):
    if n == 0:
        return -1
    pos = 0
    while (n & 1) == 0:
        n >>= 1
        pos += 1
    return pos

print("\nActivity 2: Rightmost Set Bit")
print("Rightmost set bit position in", 12, "is", rightmost_set_bit_pos(12))

# Activity 3: Check even or odd using bit
def is_even(n):
    return (n & 1) == 0

print("\nActivity 3: Even/Odd Check")
for i in [4, 7, 10, 15]:
    print(f"{i} is even: {is_even(i)}")
