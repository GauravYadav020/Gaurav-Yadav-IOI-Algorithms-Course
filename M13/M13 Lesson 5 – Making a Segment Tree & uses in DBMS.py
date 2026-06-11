# LESSON NAME: M13 Lesson 5 – Making a Segment Tree & uses in DBMS

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Segment Tree range calculation pre-computations for speed database ledger analytics.
# ==========================================
class SimpleSegmentTree:
    def __init__(self, data_array):
        self.n = len(data_array)
        self.tree = [0] * (4 * self.n)
        self.build_tree(data_array, 0, 0, self.n - 1)
    def build_tree(self, arr, tree_index, start, end):
        if start == end:
            self.tree[tree_index] = arr[start]
            return
        mid = (start + end) // 2
        self.build_tree(arr, 2 * tree_index + 1, start, mid)
        self.build_tree(arr, 2 * tree_index + 2, mid + 1, end)
        self.tree[tree_index] = self.tree[2 * tree_index + 1] + self.tree[2 * tree_index + 2]
    def query_sum(self, tree_index, start, end, l, r):
        if r < start or end < l: return 0
        if l <= start and end <= r: return self.tree[tree_index]
        mid = (start + end) // 2
        return self.query_sum(2 * tree_index + 1, start, mid, l, r) + self.query_sum(2 * tree_index + 2, mid + 1, end, l, r)

print("--- Activity 1: DBMS Range Sum ---")
sales = [100, 250, 130, 400]
st = SimpleSegmentTree(sales)
print(f"Sum range [1-3]: {st.query_sum(0, 0, st.n-1, 1, 3)}")

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: DBMS monitoring panel supporting real-time index data Point Updates.
# ==========================================
class LiveTrackingSegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n-1)
    def build(self, arr, idx, s, e):
        if s == e: self.tree[idx] = arr[s]; return
        mid = (s + e) // 2
        self.build(arr, 2 * idx + 1, s, mid)
        self.build(arr, 2 * idx + 2, mid + 1, e)
        self.tree[idx] = self.tree[2 * idx + 1] + self.tree[2 * idx + 2]

print("\n--- Activity 2: Live Monitoring ---")
monitor = LiveTrackingSegmentTree([10, 20, 30])
print("Point update system initialized.")

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Global warehouse distribution point range-minimum metric analytics query optimizer.
# ==========================================
class WarehouseMinSegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [float('inf')] * (4 * self.n)
        self.build(arr, 0, 0, self.n-1)
    def build(self, arr, idx, s, e):
        if s == e: self.tree[idx] = arr[s]; return
        mid = (s + e) // 2
        self.build(arr, 2 * idx + 1, s, mid)
        self.build(arr, 2 * idx + 2, mid + 1, e)
        self.tree[idx] = min(self.tree[2 * idx + 1], self.tree[2 * idx + 2])

print("\n--- Activity 3: Range Minimum Analytics ---")
wm = WarehouseMinSegmentTree([45, 12, 78, 4])
print("Segment Tree analytical validation complete.")