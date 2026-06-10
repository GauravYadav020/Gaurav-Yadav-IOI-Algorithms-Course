# M7 Lesson 2 – Binary Search
# =====================================
# Binary Search works on sorted arrays.
# It repeatedly divides the search interval in half.
# Time Complexity: O(log n)

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example
sorted_list = [10, 20, 30, 40, 50, 60, 70]
print("Binary Search Example:")
print(binary_search(sorted_list, 40))  # Expected: 3

# =====================================
# ACTIVITY 1: Implement Recursive Binary Search
print("\n--- Activity 1 ---")
def binary_search_recursive(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

print(binary_search_recursive(sorted_list, 60))

# =====================================
# ACTIVITY 2: Find the Insertion Point (Lower Bound)
print("\n--- Activity 2 ---")
def insertion_point(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

print(insertion_point([1, 3, 5, 7], 4))  # Should return 2

# =====================================
# ACTIVITY 3: Count Elements Less Than Target
print("\n--- Activity 3 ---")
def count_less_than(arr, target):
    return insertion_point(arr, target)

print(count_less_than([10, 20, 30, 40], 25))  # Expected: 2

print("\nLesson 2 Completed! Binary Search is very powerful on sorted data.")