"""
M4 Lesson 1 – Introduction to Bit Manipulation

Bit Manipulation is a technique to work directly with bits (0s and 1s) using bitwise operators.
This is very efficient for many problems involving numbers.
"""

# Bitwise Operators in Python
print("=== Bitwise Operators Demo ===")

a = 5  # Binary: 0101
b = 3  # Binary: 0011

print(f"a = {a} ({bin(a)}), b = {b} ({bin(b)})")

# AND (&)
print("a & b =", a & b, bin(a & b))

# OR (|)
print("a | b =", a | b, bin(a | b))

# XOR (^)
print("a ^ b =", a ^ b, bin(a ^ b))

# NOT (~)
print("~a =", ~a, bin(~a))

# Left Shift (<<)
print("a << 1 =", a << 1, bin(a << 1))

# Right Shift (>>)
print("a >> 1 =", a >> 1, bin(a >> 1))

# Activity 1: Convert number to binary and count set bits (1s)
def count_set_bits(n):
    """Count number of 1s in binary representation"""
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

print("\n=== Activity 1 ===")
num = 13  # 1101
print(f"Number of set bits in {num} ({bin(num)}) is", count_set_bits(num))

# Activity 2: Check if a number is power of 2
def is_power_of_two(n):
    """Check if number is power of 2 using bit trick"""
    return n > 0 and (n & (n-1)) == 0

print("\n=== Activity 2 ===")
for i in [8, 16, 7, 32]:
    print(f"Is {i} power of 2? {is_power_of_two(i)}")

# Activity 3: Swap two numbers without temporary variable
def swap_without_temp(x, y):
    """Swap using XOR"""
    x = x ^ y
    y = x ^ y
    x = x ^ y
    return x, y

print("\n=== Activity 3 ===")
x, y = 10, 25
print(f"Before swap: x={x}, y={y}")
x, y = swap_without_temp(x, y)
print(f"After swap: x={x}, y={y}")
