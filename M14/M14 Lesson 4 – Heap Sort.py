# LESSON NAME: M14 Lesson 4 – Heap Sort

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Write a basic sorting engine that picks numbers in descending order 
# using standard heap interactions via built-in packages.
# ==========================================
import heapq

def simple_heap_sort_descending(arr):
    # Using negative values to leverage a min-heap structure for descending outputs
    transformed_heap = [-x for x in arr]
    heapq.heapify(transformed_heap)
    
    sorted_output = []
    while transformed_heap:
        sorted_output.append(-heapq.heappop(transformed_heap))
    return sorted_output

print("--- Activity 1: Simple Descending Heap Sort Engine ---")
test_scores = [34, 12, 89, 56, 4, 72]
result = simple_heap_sort_descending(test_scores)
print(f"Sorted leaderboard values: {result}")
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Implement an in-place $O(N \log N)$ Ascending Heap Sort system from scratch 
# without using external libraries, displaying state snapshots after each pass.
# ==========================================
class InPlaceHeapSorter:
    def heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]: largest = left
        if right < n and arr[right] > arr[largest]: largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    def sort(self, arr):
        n = len(arr)
        # Phase 1: Build the Heap
        for i in range((n // 2) - 1, -1, -1):
            self.heapify(arr, n, i)
        
        # Phase 2: Extract elements one by one
        print("Commencing sorting extraction sequences:")
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr, i, 0)
            print(f" -> Step index checkpoint state [{i} items remaining]: {arr}")
        return arr

print("\n--- Activity 2: Custom In-Place Ascending Sorter ---")
inventory_prices = [500, 120, 890, 430, 210]
sorter = InPlaceHeapSorter()
sorted_prices = sorter.sort(inventory_prices)
print(f"Final ordered product listing tracking sequence: {sorted_prices}")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Build a production logs sorting compiler tool designed to sort massive, 
# unsorted network data events chronologically. Track complexity metrics like operation steps.
# ==========================================
class LogTransactionCompiler:
    def __init__(self):
        self.step_counter = 0

    def compile_sort_logs(self, log_records_list):
        n = len(log_records_list)
        
        def heapify_logs(length, index):
            self.step_counter += 1
            largest = index
            l, r = 2 * index + 1, 2 * index + 2
            
            if l < length and log_records_list[l][0] > log_records_list[largest][0]: largest = l
            if r < length and log_records_list[r][0] > log_records_list[largest][0]: largest = r
            if largest != index:
                log_records_list[index], log_records_list[largest] = log_records_list[largest], log_records_list[index]
                heapify_logs(length, largest)

        for i in range((n // 2) - 1, -1, -1):
            heapify_logs(n, i)
            
        for i in range(n - 1, 0, -1):
            log_records_list[0], log_records_list[i] = log_records_list[i], log_records_list[0]
            heapify_logs(i, 0)
            
        return log_records_list

print("\n--- Activity 3: Heavy Transaction Log Sorting Engine ---")
simulated_logs = [(1609459200, "ERR-01"), (1609459100, "INF-05"), (1609459400, "WRN-12"), (1609459000, "DB-02")]
compiler = LogTransactionCompiler()
compiled_output = compiler.compile_sort_logs(simulated_logs)

print("Chronologically compiled event trace history records:")
for timestamp, tag in compiled_output:
    print(f" * Epoch code: {timestamp} -> Event tag tracking details: {tag}")
print(f"Algorithmic dynamic computation step count complexity metrics total: {compiler.step_counter}")
print("-" * 40)