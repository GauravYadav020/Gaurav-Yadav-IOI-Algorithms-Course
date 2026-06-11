# Module 14 Lesson 4: After-Class Project
# Project Name: Priority Queue Min-Heap Operational Inversion Framework

import heapq

class StreamPriorityQueueManager:
    def __init__(self): self.heap_storage = []
    def push_metric(self, val): heapq.heappush(self.heap_storage, val)
    def extract_highest_priority(self): return heapq.heappop(self.heap_storage) if self.heap_storage else None

if __name__ == "__main__":
    pq = StreamPriorityQueueManager()
    pq.push_metric(45); pq.push_metric(12); pq.push_metric(99)
    print(f"Extracted minimum node priority trace entry element tracking point: {pq.extract_highest_priority()}")