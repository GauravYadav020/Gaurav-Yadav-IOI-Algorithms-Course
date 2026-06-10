"""
M4 Lesson 2 – BitPlay 1

Basic bit operations: Set, Clear, Toggle specific bits.
"""

# Function to get ith bit
def get_ith_bit(n, i):
    """Check if ith bit is set"""
    return (n & (1 << i)) != 0

# Set ith bit
def set_ith_bit(n, i):
    return n | (1 << i)

# Clear ith bit
def clear_ith_bit(n, i):
    return n & ~(1 << i)

# Toggle ith bit
def toggle_ith_bit(n, i):
    return n ^ (1 << i)

print("=== BitPlay 1 Demo ===")
n = 13  # Binary: 1101
print(f"Original number: {n} ({bin(n)})")

print("\n=== Activity 1: Get bits ===")
for i in range(4):
    print(f"Bit {i} of {n} is {get_ith_bit(n, i)}")

print("\n=== Activity 2: Set and Clear ===")
n_set = set_ith_bit(n, 1)   # Set bit 1
print(f"After setting bit 1: {n_set} ({bin(n_set)})")
n_clear = clear_ith_bit(n, 2)  # Clear bit 2
print(f"After clearing bit 2: {n_clear} ({bin(n_clear)})")

print("\n=== Activity 3: Toggle bits ===")
n_toggle = toggle_ith_bit(n, 0)
print(f"After toggling bit 0: {n_toggle} ({bin(n_toggle)})")
