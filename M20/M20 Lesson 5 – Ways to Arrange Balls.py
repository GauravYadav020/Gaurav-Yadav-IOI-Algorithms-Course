# LESSON NAME: M20 Lesson 5 – Ways to Arrange Balls

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Implement a basic recursive arrangement explorer that counts total ways 
# to arrange balls of different types such that no two adjacent items share matching identities.
# ==========================================
def basic_ball_arrangement_finder(count_type_a, count_type_b, last_placed_type):
    # Base Case: All ball items placed successfully
    if count_type_a == 0 and count_type_b == 0: return 1
    
    ways_count = 0
    # Try placing Type A if it's available and wasn't placed in the immediate previous step
    if count_type_a > 0 and last_placed_type != 'A':
        ways_count += basic_ball_arrangement_finder(count_type_a - 1, count_type_b, 'A')
    # Try placing Type B
    if count_type_b > 0 and last_placed_type != 'B':
        ways_count += basic_ball_arrangement_finder(count_type_a, count_type_b - 1, 'B')
        
    return ways_count

print("--- Activity 1: Non-Adjacent Ball Packing Explorer ---")
pq_a, pq_b = 2, 1
print(f"Total separate ways to position items ({pq_a}A, {pq_b}B): {basic_ball_arrangement_finder(pq_a, pq_b, '')}")
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Convert the non-adjacent grouping challenge into a high-speed 3D state-caching 
# Memoization matrix layout engine to scale up configuration capabilities.
# ==========================================
class MemoizedBallArrangementEngine:
    def __init__(self):
        self.memo_cache = {}

    def calculate_cached_ways(self, p, q, r, last_type_id):
        # Unique identifier index key mapping layout configuration
        state_key = (p, q, r, last_type_id)
        if state_key in self.memo_cache: return self.memo_cache[state_key]
        
        if p == 0 and q == 0 and r == 0: return 1
        
        total_paths = 0
        if p > 0 and last_type_id != 1: total_paths += self.calculate_cached_ways(p - 1, q, r, 1)
        if q > 0 and last_type_id != 2: total_paths += self.calculate_cached_ways(p, q - 1, r, 2)
        if r > 0 and last_type_id != 3: total_paths += self.calculate_cached_ways(p, q, r - 1, 3)
            
        self.memo_cache[state_key] = total_paths
        return total_paths

print("\n--- Activity 2: 3D State Memoization Arrangement Sorter ---")
engine = MemoizedBallArrangementEngine()
print(f"Total verified path permutations calculated for counts (2, 2, 2): {engine.calculate_cached_ways(2, 2, 2, 0)}")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Build a factory inventory automation routine that runs clean input validation rules 
# and prevents runtime exceptions when empty values or zero ball types enter processing lines.
# ==========================================
def production_inventory_combinatorics_filter(count_a, count_b, count_c):
    # Filter anomalies out safely (ensure that negative values are converted to zero constraints)
    sanitized_a = max(0, count_a)
    sanitized_b = max(0, count_b)
    sanitized_c = max(0, count_c)
    
    if sanitized_a == 0 and sanitized_b == 0 and sanitized_c == 0:
        print("⚠️ INVENTORY SYSTEM ALERT: Empty allocation parameter inputs received.")
        return 0
        
    calculator = MemoizedBallArrangementEngine()
    total_valid_options = calculator.calculate_cached_ways(sanitized_a, sanitized_b, sanitized_c, 0)
    
    print(f"Factory Automation Distribution Profile Diagnostic Summary:")
    print(f" * Target Quantities Pool -> A:{sanitized_a} | B:{sanitized_b} | C:{sanitized_c}")
    print(f" * Total mathematically calculated hazard-free configuration lines: {total_valid_options}")
    return total_valid_options

print("\n--- Activity 3: Factory Inventory Linear Analytics System ---")
production_inventory_combinatorics_filter(3, -1, 2) # Handles negative input error anomalies safely
print("-" * 40)