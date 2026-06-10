# M7 Lesson 6 – General Problems
# =====================================
# Practice problems combining searching and sorting concepts

# Problem 1: Find the Kth Smallest Element
def kth_smallest(arr, k):
    arr_sorted = sorted(arr)
    return arr_sorted[k-1] if 1 <= k <= len(arr) else None

print("Kth Smallest Example:")
print(kth_smallest([7, 10, 4, 3, 20, 15], 3))  # Expected: 7

# Problem 2: Sort array by frequency of elements
from collections import Counter
def sort_by_frequency(arr):
    freq = Counter(arr)
    return sorted(arr, key=lambda x: (-freq[x], x))

print("\nSort by Frequency:")
print(sort_by_frequency([4, 5, 6, 6, 4, 3, 6, 4]))

# =====================================
# ACTIVITY 1: Find Missing Number (1 to n)
print("\n--- Activity 1 ---")
def find_missing_number(arr, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

print(find_missing_number([1, 2, 4, 5], 5))  # Expected: 3

# =====================================
# ACTIVITY 2: Two Sum using Hashmap (better than two pointer for unsorted)
print("\n--- Activity 2 ---")
def two_sum_hash(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    return None

print(two_sum_hash([2, 7, 11, 15], 9))  # Expected: (0, 1)

# =====================================
# ACTIVITY 3: Sort Colors (Dutch National Flag - 0s, 1s, 2s)
print("\n--- Activity 3 ---")
def sort_colors(nums):
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums

colors = [2, 0, 2, 1, 1, 0]
print(sort_colors(colors[:]))  # [0,0,1,1,2,2]

print("\nLesson 6 Completed! Great job on Module 7! Keep practicing.")