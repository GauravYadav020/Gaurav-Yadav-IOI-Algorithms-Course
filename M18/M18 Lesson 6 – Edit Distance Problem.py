# LESSON NAME: M18 Lesson 6 – Edit Distance Problem

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Create a basic recursive edit-distance calculator to count single-character 
# changes (Inserts, Deletes, Replacements) required to morph word configurations.
# ==========================================
def calculate_recursive_edit_distance(w1, w2, m, n):
    # Base Case: If either string is empty, we must insert/delete all characters of the other
    if m == 0: return n
    if n == 0: return m
    
    # Characters match, skip safely
    if w1[m - 1] == w2[n - 1]:
        return calculate_recursive_edit_distance(w1, w2, m - 1, n - 1)
        
    # Mismatch: branch into Insert, Delete, and Replace sub-steps
    return 1 + min(
        calculate_recursive_edit_distance(w1, w2, m, n - 1),    # Insert operation
        calculate_recursive_edit_distance(w1, w2, m - 1, n),    # Delete operation
        calculate_recursive_edit_distance(w1, w2, m - 1, n - 1)  # Replace operation
    )

print("--- Activity 1: Word Morph Mutation Counter ---")
word_x = "CAT"
word_y = "CAR"
print(f"Minimum single adjustments needed from '{word_x}' to '{word_y}': {calculate_recursive_edit_distance(word_x, word_y, len(word_x), len(word_y))}")
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Convert the Edit Distance routine into a 2D Tabulation grid layout 
# system to accelerate matching speeds for automated word correction processors.
# ==========================================
class EditDistanceTabulator:
    def compute_distance_matrix(self, target_word, source_word):
        m, n = len(target_word), len(source_word)
        matrix = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Initialize base boundary limits columns paths
        for i in range(m + 1): matrix[i][0] = i
        for j in range(n + 1): matrix[0][j] = j
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if target_word[i - 1] == source_word[j - 1]:
                    matrix[i][j] = matrix[i - 1][j - 1]
                else:
                    matrix[i][j] = 1 + min(
                        matrix[i][j - 1],   # Insertion step
                        matrix[i - 1][j],   # Deletion step
                        matrix[i - 1][j - 1] # Replacement step
                    )
        return matrix[m][n]

print("\n--- Activity 2: 2D Matrix Edit Distance Compiler ---")
spell_checker = EditDistanceTabulator()
w_target = "SUNDAY"
w_source = "SATURDAY"
print(f"Minimum edit distance metric score calculated: {spell_checker.compute_distance_matrix(w_target, w_source)} steps")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Implement an ultra-fast spelling checker lookup optimizer that scans 
# text streams, safely ignoring string blocks with negative bounds exceptions.
# ==========================================
def production_spellcheck_filter(user_input_token, dictionary_word_pool):
    if not user_input_token: return ""
    
    best_match = None
    lowest_edit_score = float('inf')
    engine = EditDistanceTabulator()
    
    for word in dictionary_word_pool:
        # Optimization heuristic: skip checking words with completely unresolvable length disparities
        if abs(len(user_input_token) - len(word)) > lowest_edit_score:
            continue
            
        current_score = engine.compute_distance_matrix(user_input_token, word)
        if current_score < lowest_edit_score:
            lowest_edit_score = current_score
            best_match = word
            
    print(f"Database Spellcheck Parsing Stream Diagnostic Summary:")
    print(f" * Input Token flagged: '{user_input_token}' | Closest Variant Found: '{best_match}' (Distance score: {lowest_edit_score})")
    return best_match

print("\n--- Activity 3: High-Performance Spelling Matcher ---")
valid_dictionary = ["python", "pycharm", "programming", "instructor"]
corrupted_token = "pithon"
production_spellcheck_filter(corrupted_token, valid_dictionary)
print("-" * 40)