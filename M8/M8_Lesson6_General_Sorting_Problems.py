"""
M8 Lesson 6 – General Sorting Problems
Advanced Problems with 3 Activities
"""

# Problem 1: Sort array with duplicates efficiently
def sort_with_duplicates(arr):
    return sorted(arr)  # Or use counting sort for integers

# Problem 2: Find kth smallest element
def kth_smallest(arr, k):
    return sorted(arr)[k-1]

# Problem 3: Sort by frequency
from collections import Counter
def sort_by_frequency(arr):
    freq = Counter(arr)
    return sorted(arr, key=lambda x: (-freq[x], x))

if __name__ == "__main__":
    print("Example 1:", sort_with_duplicates([3, 1, 3, 2, 1]))
    print("Example 2 (3rd smallest):", kth_smallest([7, 10, 4, 3, 20, 15], 3))
    print("Example 3:", sort_by_frequency([2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12]))

"""
Activity 1: Implement Counting Sort or Radix Sort for integers.
Activity 2: Solve 'Sort Colors' (Dutch National Flag) problem - 0s, 1s, 2s.
Activity 3: Implement external sort for very large files (concept + code skeleton).
"""
