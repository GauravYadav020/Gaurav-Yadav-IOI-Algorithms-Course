"""
M8 Lesson 2 – Shell Sort
Advanced Python Implementation with 3 Activities
"""

def shell_sort(arr):
    """Advanced Shell Sort with dynamic gap sequence."""
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

# Example usage
if __name__ == "__main__":
    arr = [12, 34, 54, 2, 3]
    print("Original:", arr)
    sorted_arr = shell_sort(arr[:])
    print("Sorted:", sorted_arr)

"""
Activity 1: Implement different gap sequences (e.g., Hibbard's sequence).
Activity 2: Compare performance with Insertion Sort on large random arrays.
Activity 3: Modify for descending order and handle duplicate elements efficiently.
"""
