# M7 Lesson 5 – Selection Sort
# =====================================
# Selection Sort divides the input into sorted and unsorted region.
# Repeatedly selects the smallest (or largest) element from unsorted region.

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example
numbers = [64, 25, 12, 22, 11]
print("Selection Sort Example:")
print(selection_sort(numbers[:]))

# =====================================
# ACTIVITY 1: Selection Sort for Maximum (Descending Order)
print("\n--- Activity 1 ---")
def selection_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr

print(selection_sort_desc([64, 25, 12, 22, 11]))

# =====================================
# ACTIVITY 2: Find Minimum in each pass manually
print("\n--- Activity 2 ---")
def find_min_index(arr, start):
    min_idx = start
    for i in range(start+1, len(arr)):
        if arr[i] < arr[min_idx]:
            min_idx = i
    return min_idx

# Test
test = [3, 1, 4, 1, 5]
print(find_min_index(test, 0))  # Should be 1

# =====================================
# ACTIVITY 3: Selection Sort on Custom Objects (by length of string)
print("\n--- Activity 3 ---")
def selection_sort_by_length(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if len(arr[j]) < len(arr[min_idx]):
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

words = ["python", "is", "awesome", "code"]
print(selection_sort_by_length(words[:]))

print("\nLesson 5 Completed! Selection Sort also O(n^2) but fewer swaps.")