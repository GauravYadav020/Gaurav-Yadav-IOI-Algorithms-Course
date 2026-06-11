# Module 18 Lesson 5: After-Class Project
# Project Name: Cost Horizon Path Matrix Boundary Step Minimizer

def compute_min_cost_stair_path(step_costs_array):
    n = len(step_costs_array)
    dp = [0] * n
    dp[0], dp[1] = step_costs_array[0], step_costs_array[1]
    for i in range(2, n):
        dp[i] = step_costs_array[i] + min(dp[i-1], dp[i-2])
    return min(dp[-1], dp[-2])

if __name__ == "__main__":
    print(f"Minimum net expense matrix path solution trace parameters: {compute_min_cost_stair_path([10, 15, 20])}")