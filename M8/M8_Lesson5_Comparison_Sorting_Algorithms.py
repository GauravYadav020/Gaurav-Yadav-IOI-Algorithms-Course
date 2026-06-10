"""
M8 Lesson 5 – Comparison between Sorting Algorithms
Advanced Analysis with 3 Activities
"""

import time
import random

def time_sort(func, arr):
    """Time a sorting function."""
    start = time.time()
    result = func(arr[:])
    end = time.time()
    return result, end - start

# Import sorting functions (in real use, import from other files)
# For demo:
def insertion_sort_demo(arr): 
    # Simplified for demo
    return sorted(arr)

def shell_sort_demo(arr): return sorted(arr)
def quick_sort_demo(arr): return sorted(arr)
def merge_sort_demo(arr): return sorted(arr)

if __name__ == "__main__":
    sizes = [100, 1000, 5000]
    for size in sizes:
        arr = [random.randint(1, 10000) for _ in range(size)]
        print(f"\nArray size: {size}")
        
        _, t1 = time_sort(insertion_sort_demo, arr)
        _, t2 = time_sort(shell_sort_demo, arr)
        _, t3 = time_sort(quick_sort_demo, arr)
        _, t4 = time_sort(merge_sort_demo, arr)
        
        print(f"Insertion: {t1:.6f}s")
        print(f"Shell: {t2:.6f}s")
        print(f"Quick: {t3:.6f}s")
        print(f"Merge: {t4:.6f}s")

"""
Activity 1: Create a full benchmark comparing all four sorts on different input types (sorted, reverse, random).
Activity 2: Plot performance using matplotlib (time vs size).
Activity 3: Discuss stability and space complexity in comments.
"""
