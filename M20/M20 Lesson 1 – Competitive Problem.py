# LESSON NAME: M20 Lesson 1 – Competitive Problem

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Implement a classic competitive string parsing solution 
# that tracks and eliminates matching adjacent character pairs iteratively.
# ==========================================
def basic_adjacent_cleaner(raw_string):
    stack_archive = []
    for char in raw_string:
        # If the current character matches the top of the stack, pop it (eliminate pair)
        if stack_archive and stack_archive[-1] == char:
            stack_archive.pop()
        else:
            stack_archive.append(char)
    return "".join(stack_archive)

print("--- Activity 1: Adjacent Character Pair Eliminator ---")
test_token = "abbaay"
print(f"Original: '{test_token}' -> Processed Result: '{basic_adjacent_cleaner(test_token)}'")
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Build an online judge array utility that calculates the "Prefix Sum Matrix" 
# to answer multiple coordinate range sum query inputs in constant $O(1)$ time complexity.
# ==========================================
class RangeSumQueryEngine:
    def __init__(self, data_array):
        n = len(data_array)
        self.prefix_sums = [0] * (n + 1)
        # Precompute values sequentially
        for i in range(n):
            self.prefix_sums[i + 1] = self.prefix_sums[i] + data_array[i]

    def query_range_sum(self, left_index, right_index):
        # O(1) calculation using precomputed intervals boundary metrics
        return self.prefix_sums[right_index + 1] - self.prefix_sums[left_index]

print("\n--- Activity 2: Constant Time Prefix Sum Engine ---")
dataset = [2, 4, 1, 3, 5, 7]
engine = RangeSumQueryEngine(dataset)
print(f"Range sum query for index positions 1 to 4: {engine.query_range_sum(1, 4)}")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Create a high-performance optimization script that processes 
# streaming data windows, tracking anomalous negative balance inputs without crashing.
# ==========================================
def production_stream_inversion_tracker(data_stream):
    if not data_stream:
        print("⚠️ STREAM EXCEPTION: Empty dataset passed validation constraint rules.")
        return 0
        
    running_max_sum = data_stream[0]
    current_window_sum = data_stream[0]
    
    # Implementation of Kadane's algorithm for sub-array optimization metrics
    for measurement in data_stream[1:]:
        current_window_sum = max(measurement, current_window_sum + measurement)
        running_max_sum = max(running_max_sum, current_window_sum)
        
    print(f"Production Sub-Array Optimization Profile Diagnostic Summary:")
    print(f" * Total Stream Length: {len(data_stream)} elements | Maximum Subsegment Sum: {running_max_sum}")
    return running_max_sum

print("\n--- Activity 3: High-Performance Stream Window Optimizer ---")
noisy_stream = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
production_stream_inversion_tracker(noisy_stream)
print("-" * 40)