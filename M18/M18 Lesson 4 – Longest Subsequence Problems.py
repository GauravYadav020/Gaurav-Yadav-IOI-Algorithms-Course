# LESSON NAME: M18 Lesson 4 – Longest Subsequence Problems

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Implement a basic structural validator using recursive matrix operations 
# that computes the length of the Longest Common Subsequence (LCS) between two text blocks.
# ==========================================
def calculate_recursive_lcs(str1, str2, m, n):
    # Base Case: Strings are empty
    if m == 0 or n == 0:
        return 0
        
    # Match found
    if str1[m - 1] == str2[n - 1]:
        return 1 + calculate_recursive_lcs(str1, str2, m - 1, n - 1)
        
    # Mismatch path decision tree split
    return max(
        calculate_recursive_lcs(str1, str2, m, n - 1),
        calculate_recursive_lcs(str1, str2, m - 1, n)
    )

print("--- Activity 1: Core Recursive Subsequence Length ---")
text_a = "BAT"
text_b = "CAT"
print(f"LCS length between '{text_a}' and '{text_b}': {calculate_recursive_lcs(text_a, text_b, len(text_a), len(text_b))}")
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Implement a full Bottom-Up 2D Tabulation grid matrix to compute 
# the Longest Common Subsequence length for longer corporate validation strings.
# ==========================================
class LongestCommonSubsequenceTabulator:
    def compute_lcs_grid(self, s1, s2):
        m, n = len(s1), len(s2)
        # Allocate 2D matrix storage lookup array grid layout
        grid = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    grid[i][j] = grid[i - 1][j - 1] + 1
                else:
                    grid[i][j] = max(grid[i - 1][j], grid[i][j - 1])
                    
        return grid[m][n]

print("\n--- Activity 2: 2D Matrix Subsequence Grid ---")
tabulator = LongestCommonSubsequenceTabulator()
dna_seq1 = "AGGTAB"
dna_seq2 = "GXTXAYB"
print(f"LCS sequence length result match score: {tabulator.compute_lcs_grid(dna_seq1, dna_seq2)}")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Build an advanced string analytics tracker that computes the 2D tabulation grid 
# and processes it backward to reconstruct and return the exact matching text characters.
# ==========================================
class SubsequenceStringReconstructor:
    def extract_lcs_characters(self, s1, s2):
        m, n = len(s1), len(s2)
        grid = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]: grid[i][j] = grid[i - 1][j - 1] + 1
                else: grid[i][j] = max(grid[i - 1][j], grid[i][j - 1])
                
        # Reconstruct path backward from corner element coordinate points
        lcs_chars = []
        r, c = m, n
        while r > 0 and c > 0:
            if s1[r - 1] == s2[c - 1]:
                lcs_chars.append(s1[r - 1])
                r -= 1
                c -= 1
            elif grid[r - 1][c] >= grid[r][c - 1]:
                r -= 1
            else:
                c -= 1
                
        return "".join(reversed(lcs_chars))

print("\n--- Activity 3: Subsequence String Reconstructor ---")
reconstructor = SubsequenceStringReconstructor()
string1 = "AABCC"
string2 = "XABYCC"
print(f"Extracted matching sequence text string value: '{reconstructor.extract_lcs_characters(string1, string2)}'")
print("-" * 40)