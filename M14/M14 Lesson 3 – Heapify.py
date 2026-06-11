# LESSON NAME: M14 Lesson 3 – Heapify

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Implement a localized single-node heapify tracking utility that converts 
# an altered subtree array index back into a structurally sound standard Min-Heap orientation.
# ==========================================
def min_heapify_node(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        print(f" -> Swapped index {i} with {smallest}. Current array configuration: {arr}")
        min_heapify_node(arr, n, smallest)

print("--- Activity 1: Single Node Heapify Alignment ---")
unaligned_tree = [50, 10, 20, 15, 12, 25, 30]
print(f"Unordered structure entry: {unaligned_tree}")
min_heapify_node(unaligned_tree, len(unaligned_tree), 0)
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Implement Floyd's $O(N)$ Heap Construction algorithm that builds 
# a Max-Heap from an arbitrary array, analyzing operation count footprints along the way.
# ==========================================
class OptimizedHeapBuilder:
    def __init__(self):
        self.operations = 0

    def max_heapify(self, arr, n, i):
        self.operations += 1
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]: largest = left
        if right < n and arr[right] > arr[largest]: largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.max_heapify(arr, n, largest)

    def build_max_heap(self, arr):
        n = len(arr)
        start_index = (n // 2) - 1
        print(f"Constructing Max-Heap starting from intermediate pivot parent block: Index {start_index}")
        for i in range(start_index, -1, -1):
            self.max_heapify(arr, n, i)
        return arr

print("\n--- Activity 2: Floyd $O(N)$ Max-Heap Constructor ---")
dataset = [14, 5, 23, 89, 41, 11, 2]
builder = OptimizedHeapBuilder()
sorted_heap = builder.build_max_heap(dataset)
print(f"Valid Max-Heap array configuration state: {sorted_heap}")
print(f"Total tracking recursive step count checkpoints checked: {builder.operations}")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Write an engineering profiling script that tracks performance scaling metrics 
# ($O(N)$ vs $O(N \log N)$), measuring memory and instruction counts when generating heaps from large sets.
# ==========================================
import random
import time

class HeapProfilingTestbench:
    def heapify(self, arr, n, i):
        largest = i
        l, r = 2 * i + 1, 2 * i + 2
        if l < n and arr[l] > arr[largest]: largest = l
        if r < n and arr[r] > arr[largest]: largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    def profile_floyd_method(self, data):
        arr = list(data)
        t_start = time.perf_counter()
        for i in range((len(arr) // 2) - 1, -1, -1):
            self.heapify(arr, len(arr), i)
        return (time.perf_counter() - t_start) * 1000

print("\n--- Activity 3: Heap Generation Profiling Testbench ---")
large_data_stream = [random.randint(1, 10000) for _ in range(5000)]
bench = HeapProfilingTestbench()
duration = bench.profile_floyd_method(large_data_stream)
print(f"Floyd's Heap construction algorithm duration score (5,000 items): {duration:.4f} ms")
print("-" * 40)