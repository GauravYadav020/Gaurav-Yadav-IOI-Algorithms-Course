# LESSON NAME: M19 Lesson 6 – Palindromic partitioning

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Write a basic text verification loop that uses backtracking to find 
# the fewest cuts required to slice a word string into pure palindromic substrings.
# ==========================================
def is_palindrome(text_slice):
    return text_slice == text_slice[::-1]

def recursive_palindromic_cuts(string, i, j):
    # If segment is empty or already a complete palindrome, zero cuts are needed
    if i >= j or is_palindrome(string[i:j + 1]): return 0
    
    min_cuts_needed = float('inf')
    
    for k in range(i, j):
        current_cut_cost = (recursive_palindromic_cuts(string, i, k) +
                            recursive_palindromic_cuts(string, k + 1, j) + 1)
        if current_cut_cost < min_cuts_needed:
            min_cuts_needed = current_cut_cost
            
    return min_cuts_needed

print("--- Activity 1: Palindromic Partitioning Backtracker ---")
word_token = "geek"
print(f"Minimum cuts needed for '{word_token}': {recursive_palindromic_cuts(word_token, 0, len(word_token) - 1)}")
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Convert the palindromic text-slicing logic into a high-performance 2D matrix 
# lookup layout system to eliminate redundant substring evaluations.
# ==========================================
class PalindromicPartitionTabulator:
    def calculate_min_cuts(self, target_string):
        n = len(target_string)
        if n <= 1: return 0
        
        # pal_matrix[i][j] stores boolean flags marking if substring target_string[i..j] is a palindrome
        pal_matrix = [[False] * n for _ in range(n)]
        cuts_table = [0] * n
        
        for i in range(n): pal_matrix[i][i] = True
            
        for current_len in range(2, n + 1):
            for i in range(n - current_len + 1):
                j = i + current_len - 1
                if current_len == 2:
                    pal_matrix[i][j] = (target_string[i] == target_string[j])
                else:
                    pal_matrix[i][j] = (target_string[i] == target_string[j]) and pal_matrix[i + 1][j - 1]
                    
        for i in range(n):
            if pal_matrix[0][i]:
                cuts_table[i] = 0
            else:
                cuts_table[i] = float('inf')
                for j in range(i):
                    if pal_matrix[j + 1][i] and cuts_table[j] + 1 < cuts_table[i]:
                        cuts_table[i] = cuts_table[j] + 1
                        
        return cuts_table[n - 1]

print("\n--- Activity 2: 2D Matrix Partition Tabulator ---")
tab_processor = PalindromicPartitionTabulator()
test_token = "abcde"
print(f"Minimum partitioning slice adjustments required for '{test_token}': {tab_processor.calculate_min_cuts(test_token)} cuts")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Implement an optimized spellcheck/text utility that runs clean string conversions, 
# ignoring empty blocks and preventing crash conditions across noisy input streams.
# ==========================================
def production_stream_partition_filter(dirty_text_token):
    # Filter anomalies out safely (strip white space and filter out alpha-numeric blocks)
    sanitized_token = "".join(char for char in dirty_text_token if char.isalnum()).lower()
    
    if not sanitized_token:
        print("⚠️ STRING EXCEPTION WARNING: Empty text token sequence passed constraint rules validation.")
        return 0
        
    engine = PalindromicPartitionTabulator()
    resolved_cuts = engine.calculate_minimum_pieces = engine.calculate_min_cuts(sanitized_token)
    
    print(f"Database Text Partitioning Parsing Diagnostic Summary:")
    print(f" * Cleaned Token Target: '{sanitized_token}' | Minimum Safe Split Cuts Count: {resolved_cuts}")
    return resolved_cuts

print("\n--- Activity 3: High-Performance Text Stream Filter ---")
corrupted_input = "  A#b@b_A  "  # Sanitizes down cleanly to "abba" (a complete palindrome)
production_stream_partition_filter(corrupted_input)
print("-" * 40)