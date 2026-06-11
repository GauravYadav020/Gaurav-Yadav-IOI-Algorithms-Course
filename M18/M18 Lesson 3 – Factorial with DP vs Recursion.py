# LESSON NAME: M18 Lesson 3 – Factorial with DP vs Recursion

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Write a classic recursive Factorial script and track its active 
# program Call-Stack frames during execution.
# ==========================================
def recursive_factorial_trace(n):
    print(f" -> Entering Call-Stack Frame Layer: Factorial({n})")
    if n <= 1:
        return 1
    result = n * recursive_factorial_trace(n - 1)
    print(f" <- Collapsing Call-Stack Frame Layer: Factorial({n}) = {result}")
    return result

print("--- Activity 1: Recursive Factorial Stack Trace ---")
recursive_factorial_trace(4)
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Convert the Factorial problem into an iterative, tabular format 
# to save processing overhead and completely prevent Call-Stack Overflow crashes.
# ==========================================
class SafeTabularFactorial:
    def calculate_factorial(self, n):
        if n < 0: return 0
        if n <= 1: return 1
        
        # Dynamic table lookup setup allocation
        dp_table = [1] * (n + 1)
        
        print("Filling DP array elements sequentially:")
        for idx in range(2, n + 1):
            dp_table[idx] = idx * dp_table[idx - 1]
            print(f" -> Index [{idx}] assigned value context: {dp_table[idx]}")
            
        return dp_table[n]

print("\n--- Activity 2: Linear Tabular Factorial Array ---")
factorial_engine = SafeTabularFactorial()
print(f"Final compiled Factorial value: {factorial_engine.calculate_factorial(6)}")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Build a high-performance system simulation tool that tests call-stack 
# threshold limitations, showing how iterative Tabulation bypasses Python's maximum recursion limit.
# ==========================================
import sys

def test_system_stack_limits():
    large_input = 2000
    print(f"Active System Recursion Depth Limit Rule: {sys.getrecursionlimit()}")
    print(f"Attempting calculating value for N={large_input} via iterative Tabulation...")
    
    # Iterative Tabulation calculation bypasses standard stack overflow frames completely
    prod_accum = 1
    for step in range(2, large_input + 1):
        prod_accum *= step
        
    print(f" 🎉 SUCCESS! Computed massive factorial representation character digit count: {len(str(prod_accum))} positions")

print("\n--- Activity 3: Hardware System Stack Safeguard ---")
test_system_stack_limits()
print("-" * 40)