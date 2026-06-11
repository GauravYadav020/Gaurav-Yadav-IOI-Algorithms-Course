# LESSON NAME: M18 Lesson 2 – Introduction to Memoization and Tabulation

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Create a Top-Down Memoization function that caches values 
# in a dictionary to solve the Fibonacci sequence efficiently.
# ==========================================
class MemoizedFibonacci:
    def __init__(self):
        self.cache = {}

    def compute_top_down(self, n):
        if n in self.cache: return self.cache[n]
        if n <= 0: return 0
        if n == 1: return 1
        
        # Calculate and store to cache map entry
        self.cache[n] = self.compute_top_down(n - 1) + self.compute_top_down(n - 2)
        return self.cache[n]

print("--- Activity 1: Top-Down Memoization Cache ---")
fib_top = MemoizedFibonacci()
print(f"Memoized calculation value for Fib(50): {fib_top.compute_top_down(50)}")
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Implement a Bottom-Up Tabulation engine that builds an iterative 
# table matrix array to compute the exact same Fibonacci value without recursion.
# ==========================================
class TabulatedFibonacci:
    def compute_bottom_up(self, n):
        if n <= 0: return 0
        if n == 1: return 1
        
        # Allocate explicit table array
        table = [0] * (n + 1)
        table[1] = 1
        
        # Iteratively build states up sequentially
        for i in range(2, n + 1):
            table[i] = table[i - 1] + table[i - 2]
            
        return table[n]

print("\n--- Activity 2: Bottom-Up Tabulation Engine ---")
fib_bottom = TabulatedFibonacci()
print(f"Tabulated matrix calculation value for Fib(50): {fib_bottom.compute_bottom_up(50)}")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Write an optimization tracking script that analyzes and prints 
# memory allocation size differences between a full Tabulation table array and an O(1) Space variable rotation layout.
# ==========================================
import sys

def benchmark_dp_memory_footprint(n=1000):
    # Full Tabulation Array Matrix Memory Layout
    full_table = [0] * (n + 1)
    full_table[1] = 1
    for i in range(2, n + 1):
        full_table[i] = full_table[i-1] + full_table[i-2]
        
    # Space-Optimized Pointer Variable Rotation Layout
    prev2, prev1 = 0, 1
    for i in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
        
    print(f"Memory Allocations comparison benchmark metrics for size N={n}:")
    print(f" * Standard Tabulation Table Object Size: {sys.getsizeof(full_table)} bytes")
    print(f" * Space-Optimized Variable Pointer Size: {sys.getsizeof(prev1) + sys.getsizeof(prev2)} bytes")

print("\n--- Activity 3: Resource Structural Footprint Analyzer ---")
benchmark_dp_memory_footprint()
print("-" * 40)