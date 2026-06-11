# Module 20 Lesson 3: After-Class Project
# Project Name: Tile Stacking Combinatorics 2D Structural Tabulator Matrix

def compute_tile_stack_arrangements(target_h, max_rep, total_sizes):
    mod = 1000000007
    dp = [[0] * (target_h + 1) for _ in range(total_sizes + 1)]
    for i in range(total_sizes + 1): dp[i][0] = 1
    for i in range(1, total_sizes + 1):
        for j in range(1, target_h + 1):
            res_val = 0
            for qty in range(max_rep + 1):
                if j - (qty * i) >= 0: res_val = (res_val + dp[i - 1][j - (qty * i)]) % mod
            dp[i][j] = res_val
    return dp[total_sizes][target_h]

if __name__ == "__main__":
    print(f"Compiled architectural stable layouts options score total: {compute_tile_stack_arrangements(5, 2, 3)}")