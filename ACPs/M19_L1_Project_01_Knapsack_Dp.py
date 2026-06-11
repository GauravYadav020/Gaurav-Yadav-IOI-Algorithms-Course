# Module 19 Lesson 1: After-Class Project
# Project Name: 0-1 Knapsack Classical Discrete Valuation Grid Tabulator

def compute_01_knapsack_max(values_list, weights_list, max_capacity):
    n = len(values_list)
    dp_grid = [[0] * (max_capacity + 1) for _ in range(n + 1)]
    for item_idx in range(1, n + 1):
        for capacity_step in range(1, max_capacity + 1):
            if weights_list[item_idx - 1] <= capacity_step:
                dp_grid[item_idx][capacity_step] = max(
                    values_list[item_idx - 1] + dp_grid[item_idx - 1][capacity_step - weights_list[item_idx - 1]],
                    dp_grid[item_idx - 1][capacity_step]
                )
            else:
                dp_grid[item_idx][capacity_step] = dp_grid[item_idx - 1][capacity_step]
    return dp_grid[n][max_capacity]

if __name__ == "__main__":
    v, w = [60, 100, 120], [10, 20, 30]
    print(f"Discrete optimal item choice combinations sum score: ${compute_01_knapsack_max(v, w, 50)}")