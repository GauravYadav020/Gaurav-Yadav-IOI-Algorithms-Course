"""
M8 Lesson 1 – Insertion Sort
Advanced Python Implementation with 3 Activities
"""

def insertion_sort(arr):
    """Advanced Insertion Sort with visualization comments and edge cases."""
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Shift elements greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    print("Original:", arr)
    sorted_arr = insertion_sort(arr[:])  # Copy to avoid modifying original
    print("Sorted:", sorted_arr)

"""
Activity 1: Modify insertion sort to sort in descending order.
Activity 2: Implement insertion sort for a list of strings (lexicographical order).
Activity 3: Analyze time complexity - implement a counter for comparisons and shifts.
"""
