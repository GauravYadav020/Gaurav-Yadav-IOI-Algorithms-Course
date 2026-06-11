# Module 19 Lesson 5: After-Class Project
# Project Name: Boolean Knapsack Target Partition Subset Validator

def verify_subset_sum_target(elements_pool, target_sum_value):
    n = len(elements_pool)
    dp = [[False] * (target_sum_value + 1) for _ in range(n + 1)]
    for i in range(n + 1): dp[i][0] = True
        
    for i in range(1, n + 1):
        for j in range(1, target_sum_value + 1):
            if elements_pool[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - elements_pool[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][target_sum_value]

if __name__ == "__main__":
    print(f"Is subset matching structural target combinations partition located? {verify_subset_sum_target([3, 34, 4, 12, 5, 2], 9)}")