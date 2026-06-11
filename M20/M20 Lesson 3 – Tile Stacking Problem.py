# LESSON NAME: M20 Lesson 3 – Tile Stacking Problem

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Implement a basic recursive combinatorics utility to calculate 
# total ways to stack tiles up to a stable maximum building target height.
# ==========================================
def basic_tile_stack_counter(target_height, max_tiles_per_size, available_sizes_count):
    # Base Case Targets
    if target_height == 0: return 1
    if target_height < 0 or available_sizes_count <= 0: return 0
    
    total_combinations = 0
    # Iterate through allowed repetition counts for the current size layer
    for qty in range(max_tiles_per_size + 1):
        total_combinations += basic_tile_stack_counter(
            target_height - (qty * available_sizes_count), 
            max_tiles_per_size, 
            available_sizes_count - 1
        )
    return total_combinations

print("--- Activity 1: Tile Stacking Combinatorics Pivot ---")
h, max_k, n_sizes = 3, 2, 3
print(f"Total ways to build stack: {basic_tile_stack_counter(h, max_k, n_sizes)}")
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Create a 2D Tabulation grid matrix layout engine to solve 
# the Tile Stacking problem for larger target structures, avoiding recursive bottlenecks.
# ==========================================
class TileStackTabulator:
    def compute_stable_arrangements(self, target_h, max_rep, total_sizes):
        # dp[i][j] stores combinations to reach height j using first i tile sizes
        dp = [[0] * (target_h + 1) for _ in range(total_sizes + 1)]
        for i in range(total_sizes + 1): dp[i][0] = 1
            
        print("Tabulating structural configurations row-by-row:")
        for size_idx in range(1, total_sizes + 1):
            for height_j in range(1, target_h + 1):
                ways_sum = 0
                for qty in range(max_rep + 1):
                    if height_j - (qty * size_idx) >= 0:
                        ways_sum += dp[size_idx - 1][height_j - (qty * size_idx)]
                dp[size_idx][height_j] = ways_sum
            print(f" -> Completed processing row for tile size scale [{size_idx}]")
                
        return dp[total_sizes][target_h]

print("\n--- Activity 2: 2D Matrix Tile Stacking Tabulator ---")
tabulator = TileStackTabulator()
print(f"Compiled structural arrangements result score: {tabulator.compute_stable_arrangements(5, 2, 3)}")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Build an advanced architecture calculation simulator that logs 
# structural memory space sizes and prevents data overflow via modular calculations.
# ==========================================
import sys

def structural_load_calculator_simulation(height_target, max_repeats, sizing_options_count):
    modulus_boundary = 1000000007
    
    # Space optimization using prefix sum transformations inside tabulation array pipelines
    dp = [[0] * (height_target + 1) for _ in range(sizing_options_count + 1)]
    for i in range(sizing_options_count + 1): dp[i][0] = 1
        
    for i in range(1, sizing_options_count + 1):
        for j in range(1, height_target + 1):
            # Apply standard modular math rules safely to handle astronomical combinations
            res_val = 0
            for k in range(max_repeats + 1):
                if j - (k * i) >= 0:
                    res_val = (res_val + dp[i - 1][j - (k * i)]) % modulus_boundary
            dp[i][j] = res_val
            
    print("Architecture Optimization System Report Summary:")
    print(f" * Array Element Storage Frame Allocation Size: {sys.getsizeof(dp)} bytes")
    print(f" * Final Safe Modular Calculations Total: {dp[sizing_options_count][height_target]}")

print("\n--- Activity 3: High-Performance Architectural Modulus Engine ---")
structural_load_calculator_simulation(8, 3, 4)
print("-" * 40)