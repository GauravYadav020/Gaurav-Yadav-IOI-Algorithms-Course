# LESSON NAME: M20 Lesson 2 – Activity selection problem

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Create a basic interval analyzer that selects the maximum 
# number of non-overlapping tasks assuming they are already pre-sorted by end times.
# ==========================================
def basic_activity_analyzer(starts_arr, ends_arr):
    selected_tasks = [0]
    last_completion_time = ends_arr[0]
    
    for idx in range(1, len(starts_arr)):
        # If start time is greater or equal to previous completion time
        if starts_arr[idx] >= last_completion_time:
            selected_tasks.append(idx)
            last_completion_time = ends_arr[idx]
            
    return selected_tasks

print("--- Activity 1: Pre-Sorted Task Selection Lineup ---")
starts = [1, 3, 2, 5, 8]
ends   = [2, 4, 5, 7, 9]
print(f"Selected non-overlapping task indices: {basic_activity_analyzer(starts, ends)}")
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Implement an automated lab resource scheduler that processes 
# unsorted timestamp tuples, grouping items explicitly by their wrap-up parameters.
# ==========================================
class LabResourceScheduler:
    def arrange_max_appointments(self, dynamic_appointments):
        # Format: (Reservation_ID, StartHour, FinishHour)
        # Sort items explicitly using a greedy strategy based on finishing bounds
        dynamic_appointments.sort(key=lambda x: x[2])
        
        approved_bookings = [dynamic_appointments[0]]
        current_marker_limit = dynamic_appointments[0][2]
        
        print("Evaluating non-overlapping appointment sequences:")
        for idx in range(1, len(dynamic_appointments)):
            res_id, start, finish = dynamic_appointments[idx]
            if start >= current_marker_limit:
                approved_bookings.append(dynamic_appointments[idx])
                current_marker_limit = finish
                print(f" -> Approved: '{res_id}' [Interval: {start} to {finish}]")
                
        return approved_bookings

print("\n--- Activity 2: Unsorted Appointment Completion Optimizer ---")
raw_reservations = [('Lab-A', 5, 9), ('Lab-B', 1, 2), ('Lab-C', 3, 4), ('Lab-D', 0, 6)]
scheduler = LabResourceScheduler()
final_schedule = scheduler.arrange_max_appointments(raw_reservations)
print(f"Total compiled safe resource allocations count: {len(final_schedule)}")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Build a high-performance timeline auditor that screens out 
# invalid negative ranges and measures scheduling execution times in milliseconds.
# ==========================================
import time

def high_performance_timeline_auditor(intervals_stream):
    t_start = time.perf_counter()
    
    # Filter anomalies out safely (validate bounds: values must be positive and start <= finish)
    sanitized_timeline = [block for block in intervals_stream if block[0] >= 0 and block[1] >= block[0]]
    sanitized_timeline.sort(key=lambda x: x[1])
    
    allocated_count = 0
    timeline_marker = -1
    
    for start, finish in sanitized_timeline:
        if start >= timeline_marker:
            allocated_count += 1
            timeline_marker = finish
            
    duration = (time.perf_counter() - t_start) * 1000
    print(f"Timeline Processing Metrics:")
    print(f" * Filtered out {len(intervals_stream) - len(sanitized_timeline)} corrupted data rows.")
    print(f" * Computational execution loop length: {duration:.4f} ms")
    return allocated_count

print("\n--- Activity 3: High-Performance Timeline Auditor ---")
noisy_intervals = [(3, 5), (-1, 4), (1, 2), (6, 5), (5, 8)]
print(f"Total valid scheduled events: {high_performance_timeline_auditor(noisy_intervals)}")
print("-" * 40)