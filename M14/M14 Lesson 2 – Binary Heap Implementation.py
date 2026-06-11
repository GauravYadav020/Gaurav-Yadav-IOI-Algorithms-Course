# LESSON NAME: M14 Lesson 2 – Binary Heap Implementation

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Implement a full array-based pointer translation system 
# that reports parent, left child, and right child positions within a Binary Heap storage layout.
# ==========================================
class HeapPointerCalculator:
    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)

    def report_relationships(self, index):
        if index < 0 or index >= self.size:
            print("Invalid element tracking target index requested.")
            return
        
        parent = (index - 1) // 2 if index > 0 else "None (Root element)"
        left = 2 * index + 1 if (2 * index + 1) < self.size else "None (Terminal Leaf)"
        right = 2 * index + 2 if (2 * index + 2) < self.size else "None (Terminal Leaf)"
        
        print(f"Target Node Index [{index}] Value: {self.arr[index]}")
        print(f" -> Parent position: {parent}")
        print(f" -> Left Child position: {left}")
        print(f" -> Right Child position: {right}")

print("--- Activity 1: Binary Heap Layout Pointer Analysis ---")
mock_heap = [100, 85, 75, 40, 30, 60, 50]
calculator = HeapPointerCalculator(mock_heap)
calculator.report_relationships(1)
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Build a clean, complete Max-Heap structure tracking emergency room 
# patient triage codes. Include comprehensive array-shifting bubble-down methods from scratch.
# ==========================================
class HospitalTriageMaxHeap:
    def __init__(self):
        self.heap = []

    def extract_highest_triage(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
            
        root_item = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return root_item

    def _bubble_down(self, index):
        n = len(self.heap)
        largest = index
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            
            if left < n and self.heap[left][0] > self.heap[largest][0]:
                largest = left
            if right < n and self.heap[right][0] > self.heap[largest][0]:
                largest = right
                
            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break

print("\n--- Activity 2: Hospital Triage Array Extractor ---")
triage_system = HospitalTriageMaxHeap()
triage_system.heap = [(9, "Severe Trauma"), (7, "High Fever"), (4, "Sprained Ankle"), (2, "Minor Cut")]
print(f"Processing triage order patient event: {triage_system.extract_highest_triage()}")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Construct an advanced, fully production-grade interactive Max-Heap 
# engine complete with dynamic threshold tracking capacity rules and real-time debug visualization.
# ==========================================
class ProductionMaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def _sift_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] > self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def display_tree_visualization(self):
        print(f"Raw array storage configuration: {self.heap}")
        n = len(self.heap)
        level = 0
        while (2**level) - 1 < n:
            start = (2**level) - 1
            end = min(n, (2**(level+1)) - 1)
            print(f"Layer level {level}: {self.heap[start:end]}")
            level += 1

print("\n--- Activity 3: Interactive Max-Heap Terminal Visualizer ---")
engine = ProductionMaxHeap()
for val in [45, 99, 12, 78, 56]:
    engine.insert(val)
engine.display_tree_visualization()
print("-" * 40)