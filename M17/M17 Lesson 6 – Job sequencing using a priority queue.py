# LESSON NAME: M17 Lesson 6 – Job sequencing using a priority queue

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Write a basic priority queue insertion scheduler using min-heaps 
# to order a stream of tasks based on their profit margins.
# ==========================================
import heapq

def simple_priority_job_log(jobs):
    # Format: (Profit, JobID)
    heap = []
    for profit, name in jobs:
        # Use negative values to simulate Max-Priority using standard Min-Heap
        heapq.heappush(heap, (-profit, name))
        
    print("Flushing prioritized tasks order sequence:")
    while heap:
        prof, identifier = heapq.heappop(heap)
        print(f" -> Extracted Task: {identifier} with Priority margin level: {-prof}")

print("--- Activity 1: Direct Heap-Driven Task Registry ---")
incoming_jobs = [(40, "Task-A"), (100, "Task-B"), (70, "Task-C")]
simple_priority_job_log(incoming_jobs)
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Implement an optimized greedy job scheduling dispatcher 
# that uses a Min-Heap priority queue to track deadlined task slots efficiently.
# ==========================================
class HeapJobSequencer:
    def arrange_optimal_sequence(self, input_jobs_matrix):
        # Structure format layout parameters: (Job_ID, MaxDeadlineLimit, RevenueProfit)
        # Sort items primarily ascending by deadline properties
        input_jobs_matrix.sort(key=lambda x: x[1])
        
        active_slots_heap = []
        
        print("Evaluating timelines via heap-inversion mapping:")
        for job_id, limit, revenue in input_jobs_matrix:
            # Add profit to the priority queue
            heapq.heappush(active_slots_heap, (revenue, job_id))
            
            # If the number of scheduled jobs exceeds the current deadline limit, 
            # drop the lowest-profit job from our schedule selection list.
            if len(active_slots_heap) > limit:
                dropped = heapq.heappop(active_slots_heap)
                print(f" -> Deadline constraint overflow! Dropped low profit task: '{dropped[1]}' (${dropped[0]})")
                
        final_profit = sum(item[0] for item in active_slots_heap)
        return [item[1] for item in active_slots_heap], final_profit

print("\n--- Activity 2: Time-Bounded Heap Job Sequencer ---")
complex_jobs_pool = [('J1', 2, 60), ('J2', 1, 100), ('J3', 3, 20), ('J4', 2, 40), ('J5', 1, 200)]
sequencer = HeapJobSequencer()
final_jobs, net_cash = sequencer.arrange_optimal_sequence(complex_jobs_pool)
print(f"Optimized Dispatch Line: {final_jobs} | Total Secured Income Value: ${net_cash}")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Build a high-performance Operating System Kernel task scheduler 
# that leverages automated tie-breaking variables to handle items with matching priority weights.
# ==========================================
class KernelProcessTaskNode:
    def __init__(self, identifier, profit_score, insertion_sequence_id):
        self.id = identifier
        self.profit = profit_score
        self.seq_id = insertion_sequence_id

    def __lt__(self, other):
        # Max-heap comparison logic: Higher profit comes first.
        # Tie-breaker logic: Lower insertion sequence ID comes first for stability.
        if self.profit == other.profit:
            return self.seq_id < other.seq_id
        return self.profit > other.profit

print("\n--- Activity 3: High-Performance OS Kernel Scheduler ---")
kernel_queue = []
# Simulate incoming tasks with equal profit margins to test tie-breaker rules
task1 = KernelProcessTaskNode("Daemon-Log", 500, sequence_id=1)
task2 = KernelProcessTaskNode("UI-Redraw", 500, sequence_id=2)

heapq.heappush(kernel_queue, task1)
heapq.heappush(kernel_queue, task2)

dispatched = heapq.heappop(kernel_queue)
print(f" [CPU Core Dispatched] Active Process ID: {dispatched.id} (Seq Reference Order Check: {dispatched.seq_id})")
print("-" * 40)