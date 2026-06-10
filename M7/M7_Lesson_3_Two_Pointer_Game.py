# M7 Lesson 3 – Two Pointer Game
# =====================================
# Two Pointer technique is useful for sorted arrays.
# One pointer starts from beginning, another from end.

# Example: Find pair with given sum
def two_pointer_pair_sum(arr, target_sum):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return (arr[left], arr[right])
        elif current_sum < target_sum:
            left += 1
        else:
            right -= 1
    return None

sorted_arr = [1, 3, 5, 7, 9, 11]
print("Two Pointer Example:")
print(two_pointer_pair_sum(sorted_arr, 12))  # Expected: (1, 11) or similar

# =====================================
# ACTIVITY 1: Check if array is sorted using Two Pointers (though trivial)
print("\n--- Activity 1 ---")
def is_sorted_two_pointer(arr):
    left = 0
    for right in range(1, len(arr)):
        if arr[left] > arr[right]:
            return False
        left += 1
    return True

print(is_sorted_two_pointer([1, 3, 5, 7]))  # True

# =====================================
# ACTIVITY 2: Remove Duplicates from Sorted Array (In-place)
print("\n--- Activity 2 ---")
def remove_duplicates(arr):
    if not arr:
        return 0
    left = 0
    for right in range(1, len(arr)):
        if arr[right] != arr[left]:
            left += 1
            arr[left] = arr[right]
    return left + 1

nums = [1, 1, 2, 2, 3, 4, 4]
new_length = remove_duplicates(nums)
print(nums[:new_length])  # [1, 2, 3, 4]

# =====================================
# ACTIVITY 3: Find Triplet with Sum Zero (3Sum variant)
print("\n--- Activity 3 ---")
def find_triplet(arr, target=0):
    arr.sort()
    for i in range(len(arr)-2):
        left, right = i+1, len(arr)-1
        while left < right:
            s = arr[i] + arr[left] + arr[right]
            if s == target:
                return (arr[i], arr[left], arr[right])
            elif s < target:
                left += 1
            else:
                right -= 1
    return None

print(find_triplet([-1, 0, 1, 2, -1, -4]))

print("\nLesson 3 Completed! Two Pointer is great for optimization.")