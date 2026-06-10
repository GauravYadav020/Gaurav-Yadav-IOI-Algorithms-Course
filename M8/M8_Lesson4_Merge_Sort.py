"""
M8 Lesson 4 – Merge Sort
Advanced Python Implementation with 3 Activities
"""

def merge(left, right):
    """Merge two sorted halves."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr):
    """Advanced Merge Sort - stable and efficient."""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

# Example usage
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Original:", arr)
    sorted_arr = merge_sort(arr[:])
    print("Sorted:", sorted_arr)

"""
Activity 1: Implement bottom-up (iterative) Merge Sort.
Activity 2: Add inversion count while merging.
Activity 3: Optimize space usage with in-place merge (advanced).
"""
