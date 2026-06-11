# Module 19 Lesson 4: After-Class Project
# Project Name: Matrix Chain Multiplication Optimization Cost Resolver

def compute_mcm_min_cost(matrix_dimensions_sequence):
    n = len(matrix_dimensions_sequence) - 1
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for sequence_length in range(2, n + 1):
        for i in range(1, n - sequence_length + 2):
            j = i + sequence_length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + (matrix_dimensions_sequence[i - 1] * matrix_dimensions_sequence[k] * matrix_dimensions_sequence[j])
                if cost < dp[i][j]: dp[i][j] = cost
    return dp[1][n]

if __name__ == "__main__":
    print(f"Minimum scalar multiplication operations cost target boundary resolution: {compute_mcm_min_cost([10, 20, 30, 40])}")