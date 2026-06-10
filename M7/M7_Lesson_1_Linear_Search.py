# M7 Lesson 1 – Linear Search
# =====================================
# Linear Search is the simplest searching algorithm.
# It checks each element of the list one by one until the target is found or the list ends.
# Time Complexity: O(n) in worst case

def linear_search(arr, target):
    """Returns the index of target in arr, or -1 if not found"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example Usage
numbers = [10, 23, 45, 67, 89, 12, 34]
print("Linear Search Example:")
result = linear_search(numbers, 67)
print(f"Index of 67: {result}")

# =====================================
# ACTIVITY 1: Basic Linear Search Implementation
print("\n--- Activity 1 ---")
# Write a function to find if a number exists in a list and return its position

def activity1_linear_search(lst, key):
    for index, value in enumerate(lst):
        if value == key:
            return index
    return -1

test_list = [5, 3, 8, 6, 7, 2]
print(activity1_linear_search(test_list, 6))  # Expected: 3

# =====================================
# ACTIVITY 2: Count Occurrences using Linear Search
print("\n--- Activity 2 ---")
def count_occurrences(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count

scores = [90, 85, 90, 78, 90, 65]
print(f"90 appears {count_occurrences(scores, 90)} times")

# =====================================
# ACTIVITY 3: Find First and Last Occurrence
print("\n--- Activity 3 ---")
def find_first_last(arr, target):
    first = -1
    last = -1
    for i in range(len(arr)):
        if arr[i] == target:
            if first == -1:
                first = i
            last = i
    return first, last

arr = [1, 3, 5, 5, 5, 7, 9]
print(find_first_last(arr, 5))  # Expected: (2, 4)

print("\nLesson 1 Completed! Practice more linear search problems.")