# LESSON NAME: M19 Lesson 1 – 0/1 Knapsack Problem and Subset Sum

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Implement a classic 0/1 Knapsack solver using a 2D Tabulation matrix 
# to select whole, non-divisible items that maximize value without breaking capacity rules.
# ==========================================
class KnapsackTabulator:
    def solve_knapsack(self, values, weights, capacity):
        n = len(values)
        # Allocate 2D matrix storage lookup array grid layout
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for w in range(1, capacity + 1):
                if weights[i - 1] <= w:
                    # Choice tree: Include item vs Exclude item
                    dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
                else:
                    dp[i][w] = dp[i - 1][w]
                    
        return dp[n][capacity]

print("--- Activity 1: Classic 0/1 Knapsack Matrix ---")
vals = [60, 100, 120]
wts = [10, 20, 30]
cap = 50
loader = KnapsackTabulator()
print(f"Maximum calculated total value within capacity: {loader.solve_knapsack(vals, wts, cap)}")
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Build a Subset Sum utility that returns a boolean true or false 
# depending on whether an absolute mathematical match can be made from a pool of integers.
# ==========================================
class SubsetSumChecker:
    def has_matching_subset(self, integer_pool, target_sum):
        n = len(integer_pool)
        dp = [[False] * (target_sum + 1) for _ in range(n + 1)]
        
        # Base Case: A sum of 0 is always possible with an empty subset
        for i in range(n + 1): dp[i][0] = True
            
        for i in range(1, n + 1):
            for j in range(1, target_sum + 1):
                if integer_pool[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - integer_pool[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
                    
        return dp[n][target_sum]

print("\n--- Activity 2: Boolean Subset Sum Validator ---")
numbers = [3, 34, 4, 12, 5, 2]
req_sum = 9
checker = SubsetSumChecker()
print(f"Can a valid subset sum equal {req_sum}? {checker.has_matching_subset(numbers, req_sum)}")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Implement an ultra-fast, space-optimized 1D state-array tracking algorithm 
# to solve the Subset Sum problem using minimal space overhead.
# ==========================================
def optimized_subset_sum(num_list, final_sum):
    # Space optimization: Use a 1D array running backward to avoid overwriting previous step frames
    dp = [False] * (final_sum + 1)
    dp[0] = True
    
    for num in num_list:
        for j in range(final_sum, num - 1, -1):
            if dp[j - num]:
                dp[j] = True
                
    return dp[final_sum]

print("\n--- Activity 3: Space-Optimized 1D Array Tracker ---")
large_pool = [1, 5, 11, 5]
target_val = 16
print(f"Calculated 1D runtime match resolution for {target_val}: {optimized_subset_sum(large_pool, target_val)}")
print("-" * 40)