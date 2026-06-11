# LESSON NAME: M14 Lesson 5 – Priority Queue

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Implement an airline passenger boarding dispatcher queue utilizing priority values 
# where First-Class flyers bypass Economy travelers during the validation lookup operations.
# ==========================================
import heapq

class AirlineBoardingQueue:
    def __init__(self):
        self.queue = []

    def register_passenger(self, tier_rank, passenger_name):
        # Lower tier numbers indicate higher service processing priorities
        heapq.heappush(self.queue, (tier_rank, passenger_name))
        print(f"Registered passenger '{passenger_name}' into Tier group assignment level: {tier_rank}")

    def call_next_passenger(self):
        if self.queue:
            rank, name = heapq.heappop(self.queue)
            print(f" -> Now boarding: {name} (Tier Priority Rank: {rank})")
        else:
            print("No travelers currently pending in boarding pipelines.")

print("--- Activity 1: Airline Boarding Priority Dispatcher ---")
airport_gate = AirlineBoardingQueue()
airport_gate.register_passenger(3, "Bob (Economy)")
airport_gate.register_passenger(1, "Alice (First Class)")
airport_gate.register_passenger(2, "Charlie (Business)")

airport_gate.call_next_passenger()
airport_gate.call_next_passenger()
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Create an IT Emergency Ticketing System where incoming crash reports 
# are managed by priority ranks, and an automated tracking variable counts total operations.
# ==========================================
class IT_SupportTicketingDesk:
    def __init__(self):
        self.tickets_heap = []
        self.total_operations_log = 0

    def log_incident(self, severity_score, issue_description):
        self.total_operations_log += 1
        # Store inverse value to achieve Max-Heap behavior using standard Min-Heap functions
        heapq.heappush(self.tickets_heap, (-severity_score, issue_description))
        print(f"Logged Incident Severity [{severity_score}]: {issue_description}")

    def resolve_highest_emergency(self):
        self.total_operations_log += 1
        if self.tickets_heap:
            inverse_score, description = heapq.heappop(self.tickets_heap)
            return (-inverse_score, description)
        return None

print("\n--- Activity 2: Support Ticket Desk Dispatcher ---")
helpdesk = IT_SupportTicketingDesk()
helpdesk.log_incident(4, "Printer Driver Error")
helpdesk.log_incident(10, "Core Cloud Server Data Breach Failure Connection")
helpdesk.log_incident(7, "E-Commerce Payment Pipeline Timeout Delay")

resolved = helpdesk.resolve_highest_emergency()
print(f" -> Executive Dispatch Action Taken: Dispatched team to solve: '{resolved[1]}' with severity rank {resolved[0]}")
print(f"Total operational track counts recorded: {helpdesk.total_operations_log}")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Build a simulation of an Operating System Task Scheduler 
# that prioritizes processes based on CPU deadlines and execution cycle runtimes.
# ==========================================
class OS_ProcessTaskNode:
    def __init__(self, identifier, time_limit_priority, memory_footprint_bytes):
        self.id = identifier
        self.priority = time_limit_priority
        self.memory = memory_footprint_bytes

    def __lt__(self, other):
        # Ties are resolved by lower memory footprint benchmarks
        if self.priority == other.priority:
            return self.memory < other.memory
        return self.priority < other.priority

class AdvancedOSKernelScheduler:
    def __init__(self):
        self.task_pipeline = []

    def queue_process(self, process_node):
        heapq.heappush(self.task_pipeline, process_node)

    def dispatch_cycle_run(self):
        if self.task_pipeline:
            active_proc = heapq.heappop(self.task_pipeline)
            print(f" [CPU Kernel Core Executing] Process ID: {active_proc.id} (Rank: {active_proc.priority}, Mem: {active_proc.memory} bytes)")
        else:
            print("System idle loops active.")

print("\n--- Activity 3: High-Performance OS Kernel Scheduler ---")
kernel = AdvancedOSKernelScheduler()
kernel.queue_process(OS_ProcessTaskNode("SysLog-Daemon", 5, 2048))
kernel.queue_process(OS_ProcessTaskNode("UI-Window-Render", 2, 40960))
kernel.queue_process(OS_ProcessTaskNode("Security-Firewall", 2, 1024))  # Equal priority, lower memory choice

kernel.dispatch_cycle_run()
kernel.dispatch_cycle_run()
print("-" * 40)