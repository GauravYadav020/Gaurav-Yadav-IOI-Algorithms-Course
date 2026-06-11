# LESSON NAME: M17 Lesson 5 – Activity selection problem

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Implement a basic activity selector script that filters 
# non-overlapping intervals from a pre-sorted timeline array structure.
# ==========================================
def basic_activity_selector(start_times, end_times):
    # Assumes arrays are already pre-sorted by their end times
    selected_indices = [0]
    last_end_time = end_times[0]
    
    for i in range(1, len(start_times)):
        if start_times[i] >= last_end_time:
            selected_indices.append(i)
            last_end_time = end_times[i]
            
    return selected_indices

print("--- Activity 1: Pre-Sorted Interval Selector ---")
starts = [1, 3, 0, 5, 8, 5]
ends   = [2, 4, 6, 7, 9, 9]
print(f"Selected activity indices: {basic_activity_selector(starts, ends)}")
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Build an interactive conference room scheduling engine 
# that sorts unsorted dynamic event listings explicitly by their end times first.
# ==========================================
class ConferenceRoomScheduler:
    def schedule_maximum_events(self, meetings_list):
        # meetings_list layout structure list format: (Meeting_ID, StartHour, EndHour)
        # Greedy Choice: Sort ascending by execution end times
        meetings_list.sort(key=lambda x: x[2])
        
        approved_meetings_log = [meetings_list[0]]
        current_deadline_limit = meetings_list[0][2]
        
        print("Analyzing non-overlapping conference sequences:")
        for idx in range(1, len(meetings_list)):
            m_id, start, end = meetings_list[idx]
            if start >= current_deadline_limit:
                approved_meetings_log.append(meetings_list[idx])
                current_deadline_limit = end
                print(f" -> Approved Meeting: '{m_id}' [Interval: {start} to {end}]")
                
        return approved_meetings_log

print("\n--- Activity 2: End-Time Sorted Meeting Optimizer ---")
raw_meetings = [('M-Alpha', 3, 4), ('M-Beta', 0, 6), ('M-Gamma', 1, 2), ('M-Delta', 5, 7)]
scheduler = ConferenceRoomScheduler()
final_bookings = scheduler.schedule_maximum_events(raw_meetings)
print(f"Final safe non-overlapping conference lineup booking counts: {len(final_bookings)}")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Create a high-performance system routing optimizer that flags 
# bad data blocks (negative tracking variables) while profiling large intervals lists.
# ==========================================
def production_stream_interval_filter(interval_tuples_stream):
    # Filter anomalies out safely (validate that start metric matches less than or equal to finish parameters)
    sanitized_timeline = [block for block in interval_tuples_stream if block[0] >= 0 and block[1] >= block[0]]
    
    # Sort matching criteria timeline rows
    sanitized_timeline.sort(key=lambda x: x[1])
    
    allocated_count = 0
    marker_time_limit = -1
    
    for startup, completion in sanitized_timeline:
        if startup >= marker_time_limit:
            allocated_count += 1
            marker_time_limit = completion
            
    return allocated_count

print("\n--- Activity 3: High-Performance Filter Validation Tracker ---")
noisy_stream_data = [(5, 9), (1, 2), (-3, 4), (0, 6), (8, 7)] # contains corrupted rows
safe_allocations_count = production_stream_interval_filter(noisy_stream_data)
print(f"Total safe non-overlapping intervals parsed without throwing errors: {safe_allocations_count}")
print("-" * 40)