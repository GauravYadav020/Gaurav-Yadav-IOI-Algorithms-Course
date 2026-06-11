# Module 19 Lesson 2: After-Class Project
# Project Name: Longest Common Subsequence Global Alignment Matrix

def compute_lcs_length_matrix(string_x, string_y):
    m, n = len(string_x), len(string_y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if string_x[i - 1] == string_y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

if __name__ == "__main__":
    print(f"LCS structural text pattern matching index metrics overlap value: {compute_lcs_length_matrix('abcde', 'ace')}")