# M7 Lesson 4 – Bubble Sort
# =====================================
# Bubble Sort repeatedly steps through the list,
# compares adjacent elements and swaps them if in wrong order.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Example
data = [64, 34, 25, 12, 22, 11, 90]
print("Bubble Sort Example:")
print(bubble_sort(data[:]))  # copy to avoid modifying original

# =====================================
# ACTIVITY 1: Optimized Bubble Sort with Early Stop
print("\n--- Activity 1 ---")
# Already implemented above with early stop

# =====================================
# ACTIVITY 2: Bubble Sort on Strings (Lexicographical)
print("\n--- Activity 2 ---")
def bubble_sort_strings(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

fruits = ["banana", "apple", "cherry", "date"]
print(bubble_sort_strings(fruits[:]))

# =====================================
# ACTIVITY 3: Count Swaps in Bubble Sort
print("\n--- Activity 3 ---")
def bubble_sort_with_swaps(arr):
    n = len(arr)
    swaps = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
    return swaps, arr

arr = [5, 3, 8, 4, 2]
swaps, sorted_arr = bubble_sort_with_swaps(arr[:])
print(f"Total swaps: {swaps}, Sorted: {sorted_arr}")

print("\nLesson 4 Completed! Bubble Sort is simple but O(n^2).")