# LESSON NAME: M20 Lesson 6 – Minimum Number of Platform

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Implement a basic logistical transit counter that computes the 
# absolute maximum number of simultaneous trains occupying a station footprint grid.
# ==========================================
def basic_platform_estimator(arrival_hours, departure_hours):
    # Sort both timeline lists independently
    arrival_hours.sort()
    departure_hours.sort()
    
    platform_allocations_needed = 0
    max_concurrent_platforms = 0
    
    arr_idx = 0
    dep_idx = 0
    
    while arr_idx < len(arrival_hours) and dep_idx < len(departure_hours):
        # If the next train arrives before or exactly when the previous leaves, increment platform count
        if arrival_hours[arr_idx] <= departure_hours[dep_idx]:
            platform_allocations_needed += 1
            arr_idx += 1
            max_concurrent_platforms = max(max_concurrent_platforms, platform_allocations_needed)
        else:
            platform_allocations_needed -= 1
            dep_idx += 1
            
    return max_concurrent_platforms

print("--- Activity 1: Simple Train Timetable Sorter ---")
arrivals   = [900, 940, 950, 1100, 1500, 1800]
departures = [910, 1200, 1120, 1130, 1900, 2000]
print(f"Minimum platform numbers required to avoid crash bottlenecks: {basic_platform_estimator(arrivals, departures)}")
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Build an automated metro terminal tracking system that runs 
# iterative scheduling analyses, tracking resource expansions line-by-line.
# ==========================================
class MetroTerminalHubManager:
    def evaluate_station_track_capacity(self, arrival_stream, departure_stream):
        arrival_stream.sort()
        departure_stream.sort()
        
        active_tracks_in_use = 0
        peak_tracks_count_record = 0
        
        i, j = 0, 0
        print("Evaluating rolling transit schedule movements iteratively:")
        while i < len(arrival_stream) and j < len(departure_stream):
            if arrival_stream[i] <= departure_stream[j]:
                active_tracks_in_use += 1
                print(f" -> Train Arrival flagged at timestamp [{arrival_stream[i]}]. Tracks active: {active_tracks_in_use}")
                peak_tracks_count_record = max(peak_tracks_count_record, active_tracks_in_use)
                i += 1
            else:
                active_tracks_in_use -= 1
                print(f" -> Train Departure flagged at timestamp [{departure_stream[j]}]. Tracks active: {active_tracks_in_use}")
                j += 1
                
        return peak_tracks_count_record

print("\n--- Activity 2: Iterative Metro Track Capacity Tracker ---")
arr_logs = [1000, 1015, 1030]
dep_logs = [1020, 1040, 1050]
manager = MetroTerminalHubManager()
print(f"Peak simultaneous tracks required for scheduling safety: {manager.evaluate_station_track_capacity(arr_logs, dep_logs)}")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Build an advanced airport runway traffic analyzer that automatically screens 
# out malformed out-of-bounds timestamps and profiles parsing speeds.
# ==========================================
def production_runway_traffic_optimizer(flight_arrivals_list, flight_departures_list):
    t_start = time.perf_counter()
    
    # Filter anomalies out safely (ensure times fall within the standard 24-hour range: 0 to 2359)
    valid_arrivals = []
    valid_departures = []
    
    for idx in range(len(flight_arrivals_list)):
        a_time = flight_arrivals_list[idx]
        d_time = flight_departures_list[idx]
        if 0 <= a_time <= 2359 and 0 <= d_time <= 2359 and d_time >= a_time:
            valid_arrivals.append(a_time)
            valid_departures.append(d_time)
            
    valid_arrivals.sort()
    valid_departures.sort()
    
    runways_needed = 0
    peak_runways = 0
    i, j = 0, 0
    
    while i < len(valid_arrivals) and j < len(valid_departures):
        if valid_arrivals[i] <= valid_departures[j]:
            runways_needed += 1
            peak_runways = max(peak_runways, runways_needed)
            i += 1
        else:
            runways_needed -= 1
            j += 1
            
    duration = (time.perf_counter() - t_start) * 1000
    print(f"Airport Runway Logistics Analyzer Diagnostics:")
    print(f" * Removed {len(flight_arrivals_list) - len(valid_arrivals)} invalid data entries.")
    print(f" * Computed optimum safe flight runway capacity requirements: {peak_runways}")
    print(f" * Logistics processor calculation pipeline loop runtime speed: {duration:.4f} ms")
    return peak_runways

print("\n--- Activity 3: Airport Runway High-Performance Logistics System ---")
noisy_arrivals   = [900, 1250, 2500, 1300]  # Contains 2500 (invalid time out-of-bounds)
noisy_departures = [930, 1300, 1100, 1400]
production_runway_traffic_optimizer(noisy_arrivals, noisy_departures)
print("-" * 40)