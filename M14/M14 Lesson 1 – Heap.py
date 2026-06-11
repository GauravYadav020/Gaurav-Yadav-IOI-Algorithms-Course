# LESSON NAME: M14 Lesson 1 – Heap

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Implement a basic structural validator for an online gaming leaderboard 
# that checks whether an array representing scores adheres to the Max-Heap property.
# ==========================================
def check_max_heap_property(arr):
    n = len(arr)
    print(f"Analyzing score layout structure: {arr}")
    for i in range(n // 2):
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        
        if left_child < n and arr[i] < arr[left_child]:
            print(f" -> Failed: Parent index {i} ({arr[i]}) < Left Child index {left_child} ({arr[left_child]})")
            return False
        if right_child < n and arr[i] < arr[right_child]:
            print(f" -> Failed: Parent index {i} ({arr[i]}) < Right Child index {right_child} ({arr[right_child]})")
            return False
    return True

print("--- Activity 1: Leaderboard Heap Validator ---")
valid_leaderboard = [95, 80, 70, 50, 40, 60]
invalid_leaderboard = [95, 40, 70, 50, 80, 60]

print(f"Is valid max-heap leaderboard layout? {check_max_heap_property(valid_leaderboard)}")
print(f"Is valid max-heap leaderboard layout? {check_max_heap_property(invalid_leaderboard)}")
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Create a real-world dynamic server CPU task tracker that manually 
# inserts incoming load weights into a Min-Heap structure using an array-based format.
# ==========================================
class CPU_LoadTrackerMinHeap:
    def __init__(self):
        self.heap = []

    def insert_task(self, load_weight, task_name):
        self.heap.append((load_weight, task_name))
        self._bubble_up(len(self.heap) - 1)
        print(f"Scheduled Task: '{task_name}' with Load: {load_weight}")

    def _bubble_up(self, index):
        while index > 0:
            parent_idx = (index - 1) // 2
            if self.heap[index][0] < self.heap[parent_idx][0]:
                self.heap[index], self.heap[parent_idx] = self.heap[parent_idx], self.heap[index]
                index = parent_idx
            else:
                break

    def get_min_load(self):
        return self.heap[0] if self.heap else None

print("\n--- Activity 2: CPU Load Tracker ---")
tracker = CPU_LoadTrackerMinHeap()
tracker.insert_task(45, "Database Backup")
tracker.insert(15, "Security Patch Scan")
tracker.insert(85, "UI Rendering Asset")
print(f"Current lightest task pending: {tracker.get_min_load()}")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Write a monitoring system that processes a stream of network 
# packets and dynamically finds the top K highest-priority connection items using a Min-Heap.
# ==========================================
import heapq

class NetworkPacketMonitor:
    def __init__(self, k_limit):
        self.k_limit = k_limit
        self.min_heap = []

    def track_packet(self, priority_score, tracking_id):
        packet = (priority_score, tracking_id)
        if len(self.min_heap) < self.k_limit:
            heapq.heappush(self.min_heap, packet)
        elif priority_score > self.min_heap[0][0]:
            heapq.heapreplace(self.min_heap, packet)

    def get_top_packets(self):
        return sorted(self.min_heap, reverse=True)

print("\n--- Activity 3: High Priority Packet Monitor ---")
monitor = NetworkPacketMonitor(k_limit=3)
packets_stream = [(10, "TCP-1"), (50, "UDP-2"), (5, "ICMP-3"), (90, "HTTP-4"), (35, "FTP-5")]

for score, identifier in packets_stream:
    monitor.track_packet(score, identifier)

print(f"Top 3 Highest-Priority Packets currently tracked: {monitor.get_top_packets()}")
print("-" * 40)