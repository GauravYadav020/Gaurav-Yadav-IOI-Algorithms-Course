"""
M8 Lesson 3 – Quick Sort
Advanced Python Implementation with 3 Activities
"""

def quick_sort(arr, low=0, high=None):
    """Advanced Quick Sort with Lomuto partition and median-of-three pivot."""
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Median of three for better pivot
        mid = (low + high) // 2
        if arr[low] > arr[mid]:
            arr[low], arr[mid] = arr[mid], arr[low]
        if arr[low] > arr[high]:
            arr[low], arr[high] = arr[high], arr[low]
        if arr[mid] > arr[high]:
            arr[mid], arr[high] = arr[high], arr[mid]
        
        pivot = arr[mid]
        arr[mid], arr[high] = arr[high], arr[mid]  # Move pivot to end
        
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pi = i + 1
        
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr

# Example usage
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print("Original:", arr)
    sorted_arr = quick_sort(arr[:])
    print("Sorted:", sorted_arr)

"""
Activity 1: Implement randomized Quick Sort to avoid worst-case.
Activity 2: Count the number of partitions and recursions.
Activity 3: Handle already sorted arrays efficiently (add check).
"""
