# LESSON NAME: M19 Lesson 2 – Maximum sum of elements from an array with no two consecutive elements

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Create a basic recursive selector function with dynamic logs 
# that sums values from an integer list ensuring no two selected elements are adjacent.
# ==========================================
def recursive_non_consecutive_sum(arr, index):
    if index < 0: return 0
    if index == 0: return arr[0]
    
    # Choice tree: Pick current index (and skip adjacent) vs Skip current index completely
    pick = arr[index] + recursive_non_consecutive_sum(arr, index - 2)
    skip = recursive_non_consecutive_sum(arr, index - 1)
    
    return max(pick, skip)

print("--- Activity 1: Non-Consecutive Recursive Pivot ---")
sample_arr = [6, 7, 1, 3, 8, 2]
print(f"Max subset sum: {recursive_non_consecutive_sum(sample_arr, len(sample_arr) - 1)}")
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Implement an elegant 1D Dynamic Programming Tabulation array 
# that solves the non-consecutive maximum sum problem in linear time for an array of account balances.
# ==========================================
class SafeAccountBalanceTabulator:
    def maximize_secure_yield(self, balances_list):
        n = len(balances_list)
        if n == 0: return 0
        if n == 1: return balances_list[0]
        
        dp = [0] * n
        dp[0] = balances_list[0]
        dp[1] = max(balances_list[0], balances_list[1])
        
        print("Tabulating non-consecutive value constraints iteratively:")
        for i in range(2, n):
            dp[i] = max(balances_list[i] + dp[i - 2], dp[i - 1])
            print(f" -> Index position context [{i}] max linear tracking state: {dp[i]}")
            
        return dp[n - 1]

print("\n--- Activity 2: Linear Non-Adjacent Sum Tabulator ---")
accounts = [2, 10, 13, 4, 2, 15]
tab_engine = SafeAccountBalanceTabulator()
print(f"Absolute max compound sum yield: {tab_engine.maximize_secure_yield(accounts)}")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Write an ultra-efficient space-optimized pointer-rotation system 
# that tracks the non-consecutive maximum sum in $O(1)$ auxiliary memory space.
# ==========================================
def constant_space_max_sum(data_stream):
    if not data_stream: return 0
    
    inclusive_pointer = data_stream[0]
    exclusive_pointer = 0
    
    for current_val in data_stream[1:]:
        # Temp reference updates using pointer rotation transformations
        new_exclusive = max(inclusive_pointer, exclusive_pointer)
        inclusive_pointer = exclusive_pointer + current_val
        exclusive_pointer = new_exclusive
        
    return max(inclusive_pointer, exclusive_pointer)

print("\n--- Activity 3: Constant Memory O(1) Pointer Rotator ---")
stream = [5, 5, 10, 100, 10, 5]
print(f"Calculated O(1) space max sum allocation: {constant_space_max_sum(stream)}")
print("-" * 40)