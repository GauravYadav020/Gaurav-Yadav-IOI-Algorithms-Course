"""
M4 Lesson 6 – Power Set

Generate all subsets of a set using Bit Manipulation (very efficient).
"""

def generate_power_set(arr):
    """Generate power set using bit manipulation"""
    n = len(arr)
    power_set = []
    
    # 2^n subsets
    for i in range(1 << n):   # 0 to (2^n - 1)
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(arr[j])
        power_set.append(subset)
    return power_set

print("=== Power Set using Bit Manipulation ===")

# Activity 1: Basic Power Set
nums = [1, 2, 3]
print("Power Set of", nums)
for subset in generate_power_set(nums):
    print(subset)

# Activity 2: Power Set of characters
chars = ['a', 'b', 'c']
print("\nPower Set of", chars)
for subset in generate_power_set(chars):
    print(subset)

# Activity 3: Count total subsets (should be 2^n)
def count_subsets(n):
    return 1 << n   # 2**n

print("\nActivity 3:")
print("Total subsets for 4 elements:", count_subsets(4))
print("Total subsets for 5 elements:", count_subsets(5))
