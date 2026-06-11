# LESSON NAME: M20 Lesson 4 – Weighted Job Scheduling

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Implement a basic weighted timeline scheduler that finds profit metrics 
# from non-overlapping tasks using a standard linear lookup pattern.
# ==========================================
class WeightedJob:
    def __init__(self, start, end, profit):
        self.start = start
        self.end = end
        self.profit = profit

def basic_weighted_scheduler(jobs_pool):
    # Sort items explicitly based ascending on completion times
    jobs_pool.sort(key=lambda x: x.end)
    n = len(jobs_pool)
    dp = [0] * n
    dp[0] = jobs_pool[0].profit
    
    for i in range(1, n):
        include_profit = jobs_pool[i].profit
        latest_valid_index = -1
        
        # Search backward for the most recent non-overlapping job index
        for j in range(i - 1, -1, -1):
            if jobs_pool[j].end <= jobs_pool[i].start:
                latest_valid_index = j
                break
                
        if latest_valid_index != -1:
            include_profit += dp[latest_valid_index]
            
        dp[i] = max(include_profit, dp[i - 1])
    return dp[n - 1]

print("--- Activity 1: Linear Lookup Weighted Scheduler ---")
pool = [WeightedJob(1, 2, 50), WeightedJob(3, 5, 20), WeightedJob(6, 19, 100), WeightedJob(2, 100, 200)]
print(f"Maximum calculated total profit yield: ${basic_weighted_scheduler(pool)}")
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Optimize the execution step paths of your weighted job scheduling engine 
# by implementing Binary Search (`bisect`) to find overlapping timeline conflicts.
# ==========================================
import bisect

class OptimizedProductionPlanner:
    def compute_max_revenue(self, scheduled_tasks_list):
        # Format: (StartHour, FinishHour, PayoutValue)
        scheduled_tasks_list.sort(key=lambda x: x[1])
        finish_times = [task[1] for task in scheduled_tasks_list]
        
        n = len(scheduled_tasks_list)
        dp = [0] * n
        dp[0] = scheduled_tasks_list[0][2]
        
        print("Evaluating timelines via high-precision binary intervals search:")
        for i in range(1, n):
            start, finish, payout = scheduled_tasks_list[i]
            include_payout = payout
            
            # Binary search to find the highest finish time index <= current start time
            idx = bisect.bisect_right(finish_times, start) - 1
            if idx >= 0:
                include_payout += dp[idx]
                
            dp[i] = max(include_payout, dp[i - 1])
            print(f" -> Evaluated Task slot index [{i}] max revenue potential tracking: ${dp[i]}")
            
        return dp[n - 1]

print("\n--- Activity 2: Binary Search Time Planner Engine ---")
enterprise_pipeline = [(1, 3, 5), (2, 5, 6), (4, 6, 5), (6, 7, 41)]
planner = OptimizedProductionPlanner()
print(f"Optimal compound project net payouts total: ${planner.compute_max_revenue(enterprise_pipeline)}")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Build an automated profiling script that screens out completely corrupted 
# timeline data blocks (negative times or missing values) and logs system processing throughput.
# ==========================================
def production_planner_stress_test(raw_noisy_stream):
    # Filter anomalies out safely (validate bounds: tasks must have non-negative elements and valid time durations)
    sanitized_pool = [t for t in raw_noisy_stream if t[0] >= 0 and t[1] > t[0] and t[2] >= 0]
    
    if not sanitized_pool:
        print("🚨 TASK REGISTRY EXCEPTION: No valid items found after safety screening.")
        return 0
        
    t_start = time.perf_counter()
    sanitized_pool.sort(key=lambda x: x[1])
    f_times = [item[1] for item in sanitized_pool]
    
    dp = [0] * len(sanitized_pool)
    dp[0] = sanitized_pool[0][2]
    
    for i in range(1, len(sanitized_pool)):
        idx = bisect.bisect_right(f_times, sanitized_pool[i][0]) - 1
        profit_inc = sanitized_pool[i][2]
        if idx >= 0: profit_inc += dp[idx]
        dp[i] = max(profit_inc, dp[i - 1])
        
    duration = (time.perf_counter() - t_start) * 1000
    print(f"Framework Stress Test Execution Analytics Summary:")
    print(f" * Handled and removed {len(raw_noisy_stream) - len(sanitized_pool)} invalid timeline records.")
    print(f" * High precision binary scheduling pipeline loop time: {duration:.4f} ms")
    return dp[-1]

print("\n--- Activity 3: High-Performance Production Scheduler ---")
raw_stream_data = [(0, 4, 100), (2, 1, 50), (5, 8, 200), (-3, 4, 10), (7, 12, 300)] # contains safety checking constraints
print(f"Aggregated safe project execution payout result: ${production_planner_stress_test(raw_stream_data)}")
print("-" * 40)