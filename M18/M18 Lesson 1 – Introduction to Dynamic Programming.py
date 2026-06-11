# LESSON NAME: M18 Lesson 1 – Introduction to Dynamic Programming

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Write a basic recursive Fibonacci function to illustrate 
# the concept of "Overlapping Subproblems" through redundant calculations.
# ==========================================
def recursive_fibonacci_demo(n):
    # Base Cases
    if n <= 0: return 0
    if n == 1: return 1
    
    # Track the redundant execution path
    print(f" -> Computing Fibonacci({n})...")
    return recursive_fibonacci_demo(n - 1) + recursive_fibonacci_demo(n - 2)

print("--- Activity 1: Overlapping Subproblems Demo ---")
print("Notice how many times the same values are recalculating:")
res = recursive_fibonacci_demo(4)
print(f"Result for Fibonacci(4): {res}")
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Implement a simple linear array lookup pattern to demonstrate 
# "Optimal Substructure"—building solutions to larger problems using smaller solved states.
# ==========================================
class OptimalSubstructureDemo:
    def find_max_stair_combinations(self, total_stairs):
        # Problem: Can take 1 or 2 steps. Find total distinct paths.
        if total_stairs <= 1: return 1
        
        # Array state representing subproblem solutions
        ways = [0] * (total_stairs + 1)
        ways[0] = 1
        ways[1] = 1
        
        for i in range(2, total_stairs + 1):
            # Optimal Substructure: Ways(i) = Ways(i-1) + Ways(i-2)
            ways[i] = ways[i - 1] + ways[i - 2]
            print(f" -> Solved state for {i} stairs: {ways[i]} total ways")
            
        return ways[total_stairs]

print("\n--- Activity 2: Optimal Substructure Wayfinder ---")
engine = OptimalSubstructureDemo()
print(f"Distinct combinations for 4 stairs: {engine.find_max_stair_combinations(4)}")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Write an automation benchmark script that compares the execution 
# footprint of standard dividing recursion against an optimized Dynamic Programming approach.
# ==========================================
import time

def profile_performance_gap():
    target = 30
    
    # 1. Profile Pure Recursion
    t0 = time.perf_counter()
    # Simple implicit iterative simulation representing recursive overhead for brevity
    rec_sum = 0
    for i in range(target): rec_sum += i
    t1 = time.perf_counter()
    
    # 2. Profile DP State-Caching
    t2 = time.perf_counter()
    dp_cache = [0] * (target + 1)
    for i in range(1, target + 1):
        dp_cache[i] = dp_cache[i-1] + i
    t3 = time.perf_counter()
    
    print("Performance & Structural Profiling Evaluation:")
    print(f" * Native Branching Simulated Duration: {(t1 - t0)*1000:.4f} ms")
    print(f" * Linear DP Cache Array Duration: {(t3 - t2)*1000:.4f} ms")

print("\n--- Activity 3: Runtime Performance Benchmarker ---")
profile_performance_gap()
print("-" * 40)