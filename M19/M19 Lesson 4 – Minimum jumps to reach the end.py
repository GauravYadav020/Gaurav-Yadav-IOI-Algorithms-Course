# LESSON NAME: M19 Lesson 4 – Minimum jumps to reach the end

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Write a recursive pathfinder tool that calculates the minimum number 
# of index leaps required to safely cross a linear jump array topology map.
# ==========================================
def recursive_min_jumps(arr, index=0):
    # Base Case: Reached or exceeded end boundary line position
    if index >= len(arr) - 1: return 0
    if arr[index] == 0: return float('inf') # Dead end block node
    
    min_leaps = float('inf')
    max_steps_allowed = arr[index]
    
    for step in range(1, max_steps_allowed + 1):
        leaps = recursive_min_jumps(arr, index + step)
        if leaps != float('inf') and leaps + 1 < min_leaps:
            min_leaps = leaps + 1
            
    return min_leaps

print("--- Activity 1: Jump Array Recursive Pathfinder ---")
jump_grid = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(f"Minimum leaps required to traverse grid: {recursive_min_jumps(jump_grid)}")
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Implement a 1D Dynamic Programming Tabulation array 
# that stores subproblem jump metrics to accelerate calculation performance.
# ==========================================
class LinearJumpTabulator:
    def compute_fastest_jump_route(self, dynamic_jump_array):
        n = len(dynamic_jump_array)
        if n == 0 or dynamic_jump_array[0] == 0: return -1
        
        dp = [float('inf')] * n
        dp[0] = 0 # Base context: Origin takes 0 leaps
        
        print("Tabulating leap paths sequentially:")
        for i in range(1, n):
            for j in range(i):
                # If target position index can be cleared from a previous node point
                if j + dynamic_jump_array[j] >= i:
                    dp[i] = min(dp[i], dp[j] + 1)
            print(f" -> Node Index [{i}] localized min leap path: {dp[i]}")
                    
        return dp[n - 1] if dp[n - 1] != float('inf') else -1

print("\n--- Activity 2: Linear Jump Tabulation Engine ---")
tabulator = LinearJumpTabulator()
print(f"Optimal leap count result score: {tabulator.compute_fastest_jump_route([2, 3, 1, 1, 4])}")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Build an ultra-fast $O(N)$ linear-time optimization tracking script 
# that computes structural steps using a sliding-window reach index.
# ==========================================
def production_speed_jump_optimizer(coordinate_leaps_stream):
    n = len(coordinate_leaps_stream)
    if n <= 1: return 0
    if coordinate_leaps_stream[0] == 0: return -1
    
    max_reach_index = coordinate_leaps_stream[0]
    steps_remaining_in_window = coordinate_leaps_stream[0]
    jumps_counter = 1
    
    for idx in range(1, n - 1):
        max_reach_index = max(max_reach_index, idx + coordinate_leaps_stream[idx])
        steps_remaining_in_window -= 1
        
        # If current stepping scope boundary runs completely dry
        if steps_remaining_in_window == 0:
            jumps_counter += 1
            if idx >= max_reach_index: return -1 # Trapped inside dead zone loop
            steps_remaining_in_window = max_reach_index - idx
            
    return jumps_counter

print("\n--- Activity 3: High-Performance O(N) Step Optimizer ---")
massive_coordinates = [2, 3, 0, 1, 4]
print(f"Compiled absolute min tracking jump sequence count: {production_speed_jump_optimizer(massive_coordinates)}")
print("-" * 40)