# ============================================================
#        MODULE 9 - LESSON 4: DOUBLY LINKED LIST II
# ============================================================
# Topics Covered:
#   - LRU Cache implementation using DLL + HashMap
#   - Merge Sort on Doubly Linked List
#   - Rotate a DLL by K positions
#   - Flatten a multi-level DLL
# ============================================================


# ──────────────────────────────────────────────────────────
#  ACTIVITY 1 — LRU Cache using DLL + HashMap
# ──────────────────────────────────────────────────────────
"""
Problem:
    Implement an LRU (Least Recently Used) Cache with:
      - get(key)    → return value if present, else -1
      - put(key, value) → insert/update; evict LRU if full

    Strategy:
      - DLL stores (key, value) pairs; head = MRU, tail = LRU
      - HashMap { key -> DLL node } for O(1) lookup
      - On every get/put, move the accessed node to head
"""

print("=" * 60)
print("   ACTIVITY 1: LRU Cache — DLL + HashMap")
print("=" * 60)


class CacheNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}               # key -> CacheNode

        # Dummy head (MRU end) and tail (LRU end)
        self.head = CacheNode()       # dummy head
        self.tail = CacheNode()       # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    # ── Internal helpers ──

    def _remove(self, node: CacheNode):
        """Detach node from DLL."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_at_front(self, node: CacheNode):
        """Insert node right after dummy head (MRU position)."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    # ── Public API ──

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._insert_at_front(node)   # mark as recently used
        return node.value

    def put(self, key: int, value: int):
        if key in self.cache:
            self._remove(self.cache[key])
        node = CacheNode(key, value)
        self.cache[key] = node
        self._insert_at_front(node)

        if len(self.cache) > self.capacity:
            # Evict LRU — node just before dummy tail
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
            print(f"  [evict] Evicted key={lru.key} (LRU)")

    def display_cache(self):
        """Show cache from MRU to LRU."""
        items = []
        cur = self.head.next
        while cur is not self.tail:
            items.append(f"({cur.key}:{cur.value})")
            cur = cur.next
        print("  Cache [MRU→LRU]:", " -> ".join(items) if items else "EMPTY")


# ── Driver Code ──
print("\n[i] LRU Cache with capacity = 3")
lru = LRUCache(3)

print("\n[+] put(1,10), put(2,20), put(3,30):")
lru.put(1, 10); lru.put(2, 20); lru.put(3, 30)
lru.display_cache()

print("\n[+] get(1) — access key=1 (moves to MRU):")
print(f"  get(1) = {lru.get(1)}")
lru.display_cache()

print("\n[+] put(4,40) — exceeds capacity, evicts LRU:")
lru.put(4, 40)
lru.display_cache()

print("\n[+] get(2) — was evicted, should return -1:")
print(f"  get(2) = {lru.get(2)}")

print("\n[+] put(5,50) — evicts LRU again:")
lru.put(5, 50)
lru.display_cache()

print(f"\n[i] Cache size: {len(lru.cache)}")


# ──────────────────────────────────────────────────────────
#  ACTIVITY 2 — Merge Sort on Doubly Linked List
# ──────────────────────────────────────────────────────────
"""
Problem:
    Sort a doubly linked list using Merge Sort.
    Steps:
      1. Find the middle using slow-fast pointers.
      2. Split into two halves.
      3. Recursively sort each half.
      4. Merge the two sorted halves.
    Time: O(n log n)  Space: O(log n) recursion stack
"""

print("\n" + "=" * 60)
print("   ACTIVITY 2: Merge Sort on Doubly Linked List")
print("=" * 60)


class DLLNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def dll_display(head, label="DLL"):
    elems = []
    cur = head
    while cur:
        elems.append(str(cur.data))
        cur = cur.next
    print(f"  {label}: {' <-> '.join(elems)} <-> NULL" if elems else f"  {label}: NULL")


def get_middle_dll(head):
    """Returns the middle node (slow-fast pointer)."""
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge_dll(left, right):
    """Merge two sorted DLLs; returns new head."""
    if not left:
        return right
    if not right:
        return left

    if left.data <= right.data:
        result = left
        result.next = merge_dll(left.next, right)
    else:
        result = right
        result.next = merge_dll(left, right.next)

    if result.next:
        result.next.prev = result
    result.prev = None
    return result


def merge_sort_dll(head):
    """Recursively split and merge."""
    if not head or not head.next:
        return head

    mid = get_middle_dll(head)
    right_half = mid.next

    # Split
    mid.next = None
    if right_half:
        right_half.prev = None

    left_sorted = merge_sort_dll(head)
    right_sorted = merge_sort_dll(right_half)

    return merge_dll(left_sorted, right_sorted)


def build_dll(values):
    if not values:
        return None
    head = DLLNode(values[0])
    cur = head
    for v in values[1:]:
        new = DLLNode(v)
        new.prev = cur
        cur.next = new
        cur = new
    return head


# ── Driver Code ──
print("\n[i] Sorting: [5, 1, 4, 2, 8, 3, 7, 6]")
head = build_dll([5, 1, 4, 2, 8, 3, 7, 6])
dll_display(head, "Before")

sorted_head = merge_sort_dll(head)
dll_display(sorted_head, "After ")

print("\n[+] Edge: already sorted list [1,2,3,4,5]:")
h2 = build_dll([1, 2, 3, 4, 5])
dll_display(h2, "Before")
dll_display(merge_sort_dll(h2), "After ")

print("\n[+] Edge: reverse sorted [5,4,3,2,1]:")
h3 = build_dll([5, 4, 3, 2, 1])
dll_display(h3, "Before")
dll_display(merge_sort_dll(h3), "After ")

print("\n[+] Edge: single element [42]:")
h4 = build_dll([42])
dll_display(merge_sort_dll(h4), "After ")


# ──────────────────────────────────────────────────────────
#  ACTIVITY 3 — Rotate DLL by K + Flatten Multi-level DLL
# ──────────────────────────────────────────────────────────
"""
Problem:
    (a) Rotate a doubly linked list to the right by K positions.
        Example: [1,2,3,4,5], K=2 → [4,5,1,2,3]

    (b) Flatten a multi-level doubly linked list.
        Each node may have a 'child' pointer to another DLL.
        Flatten so child lists are inserted after the parent node.
"""

print("\n" + "=" * 60)
print("   ACTIVITY 3: Rotate DLL by K + Flatten Multi-level DLL")
print("=" * 60)


# ── (a) Rotate DLL by K positions ──

def rotate_dll(head, k):
    """
    Rotate DLL right by K positions.
    Strategy:
      1. Find length and tail.
      2. k = k % length (handle k > length)
      3. New tail is at (length - k) from head.
      4. Break and reconnect.
    """
    if not head or not head.next or k == 0:
        return head

    # Find length and tail
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    k = k % length
    if k == 0:
        return head

    # Find new tail: (length - k - 1) steps from head
    steps = length - k - 1
    new_tail = head
    for _ in range(steps):
        new_tail = new_tail.next

    new_head = new_tail.next

    # Break
    new_tail.next = None
    new_head.prev = None

    # Connect old tail to old head
    tail.next = head
    head.prev = tail

    return new_head


print("\n[a] Rotate [1,2,3,4,5] by K=2 (expected: [4,5,1,2,3]):")
h = build_dll([1, 2, 3, 4, 5])
dll_display(h, "Before")
rotated = rotate_dll(h, 2)
dll_display(rotated, "After ")

print("\n[+] Rotate by K=5 (full rotation, same list):")
h2 = build_dll([1, 2, 3, 4, 5])
dll_display(rotate_dll(h2, 5), "After ")

print("\n[+] Rotate by K=7 (K > length, effective K=2):")
h3 = build_dll([1, 2, 3, 4, 5])
dll_display(rotate_dll(h3, 7), "After ")


# ── (b) Flatten Multi-level DLL ──

class MultiNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        self.child = None


def flatten_multilevel(head):
    """
    Flatten multi-level DLL.
    When a node has a child, insert child list between
    current node and current.next.
    Time: O(n) where n = total nodes across all levels.
    """
    if not head:
        return head

    cur = head
    while cur:
        if cur.child:
            child_head = cur.child
            child_tail = child_head
            while child_tail.next:
                child_tail = child_tail.next

            next_node = cur.next

            # Connect cur -> child_head
            cur.next = child_head
            child_head.prev = cur
            cur.child = None

            # Connect child_tail -> next_node
            child_tail.next = next_node
            if next_node:
                next_node.prev = child_tail

        cur = cur.next
    return head


def display_multilevel(head, label="Flat"):
    elems = []
    cur = head
    while cur:
        elems.append(str(cur.val))
        cur = cur.next
    print(f"  {label}: {' <-> '.join(elems)}")


print("\n[b] Flatten Multi-level DLL:")
print("  Structure:")
print("  1 <-> 2 <-> 3 <-> 4")
print("              |")
print("              5 <-> 6")
print("                    |")
print("                    7 <-> 8")

# Build multi-level list
nodes = {i: MultiNode(i) for i in range(1, 9)}
# Level 1: 1 <-> 2 <-> 3 <-> 4
for i in [1, 2, 3]:
    nodes[i].next = nodes[i + 1]
    nodes[i + 1].prev = nodes[i]
# Level 2: 5 <-> 6 (child of 3)
nodes[3].child = nodes[5]
nodes[5].next = nodes[6]
nodes[6].prev = nodes[5]
# Level 3: 7 <-> 8 (child of 6)
nodes[6].child = nodes[7]
nodes[7].next = nodes[8]
nodes[8].prev = nodes[7]

flattened = flatten_multilevel(nodes[1])
display_multilevel(flattened, "After flattening")
print("  Expected: 1 <-> 2 <-> 3 <-> 5 <-> 6 <-> 7 <-> 8 <-> 4")
