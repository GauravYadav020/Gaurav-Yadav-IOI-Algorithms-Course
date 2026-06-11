# LESSON NAME: M17 Lesson 3 – Job Sequencing Problem

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Create a basic deadline scheduler that processes tasks 
# sequentially based on their profits, filling open execution slot positions from scratch.
# ==========================================
def simple_job_scheduler(jobs_list):
    # jobs_list structure: (Job_ID, Deadline, Profit)
    # Sort strictly descending by profit yield values
    jobs_list.sort(key=lambda x: x[2], reverse=True)
    
    max_deadline = max(job[1] for job in jobs_list)
    time_slots = [None] * (max_deadline + 1)
    
    for job_id, deadline, profit in jobs_list:
        # Try to find a free slot from the deadline backwards
        for slot in range(deadline, 0, -1):
            if time_slots[slot] == None:
                time_slots[slot] = job_id
                break
                
    return [slot for slot in time_slots if slot is not None]

print("--- Activity 1: Core Job Scheduling Sequence ---")
mock_tasks = [('JobA', 2, 100), ('JobB', 1, 19), ('JobC', 2, 27)]
print(f"Allocated basic execution pipeline tracking: {simple_job_scheduler(mock_tasks)}")
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Build a corporate project task alignment engine that tracks 
# accrued milestone financial metrics alongside full operational path breakdowns.
# ==========================================
class CorporateTaskAlignmentEngine:
    def compile_max_profit_schedule(self, jobs_matrix):
        # Format: (TaskName, EndTimeDeadline, NetProfit)
        jobs_matrix.sort(key=lambda x: x[2], reverse=True)
        
        limit_boundary = max(x[1] for x in jobs_matrix)
        schedule_ledger = [None] * limit_boundary
        total_accrued_revenue = 0
        
        print("Evaluating operational deadline slot positions:")
        for identifier, limit, revenue in jobs_matrix:
            for target_index in range(min(limit_boundary, limit) - 1, -1, -1):
                if schedule_ledger[target_index] is None:
                    schedule_ledger[target_index] = identifier
                    total_accrued_revenue += revenue
                    print(f" -> Positioned '{identifier}' in hour slot block: {target_index + 1}")
                    break
                    
        return [task for task in schedule_ledger if task], total_accrued_revenue

print("\n--- Activity 2: Enterprise Task Milestone Scheduler ---")
enterprise_pipeline = [('T-1', 4, 70), ('T-2', 1, 80), ('T-3', 1, 30), ('T-4', 1, 100), ('T-5', 3, 40)]
engine = CorporateTaskAlignmentEngine()
final_sequence, total_cash = engine.compile_max_profit_schedule(enterprise_pipeline)
print(f"Optimized Path: {final_sequence} | Aggregated Net Financial Return: ${total_cash}")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Write an optimization tracking script that analyzes structural footprints 
# (memory allocation benchmarks) and execution times across varying job loads.
# ==========================================
import sys

def benchmark_scheduling_footprint():
    simulated_jobs_pool = [(f"Task-{i}", i % 5 + 1, i * 10) for i in range(500)]
    
    t_start = time.perf_counter()
    simulated_jobs_pool.sort(key=lambda x: x[2], reverse=True)
    limit = max(x[1] for x in simulated_jobs_pool)
    slots = [None] * limit
    for id_tag, dead, prof in simulated_jobs_pool:
        for s in range(dead - 1, -1, -1):
            if slots[s] is None:
                slots[s] = id_tag
                break
    duration = (time.perf_counter() - t_start) * 1000
    
    print("Scheduling Framework Profiler Evaluation:")
    print(f" * Array Storage Footprint Size: {sys.getsizeof(slots)} bytes")
    print(f" * Processing Time for 500 Task Nodes: {duration:.4f} ms")

print("\n--- Activity 3: Resource Structural Footprint Analyzer ---")
benchmark_scheduling_footprint()
print("-" * 40)