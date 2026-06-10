# ============================================================
#        MODULE 9 - LESSON 2: LINKED LIST II
# ============================================================
# Topics Covered:
#   - Merge two sorted linked lists
#   - Detect and remove cycle (Floyd's algorithm)
#   - Remove duplicates from sorted/unsorted lists
#   - Intersection of two linked lists
# ============================================================


# ──────────────────────────────────────────────────────────
#  ACTIVITY 1 — Merge Two Sorted Linked Lists
# ──────────────────────────────────────────────────────────
"""
Problem:
    Given two sorted linked lists, merge them into a single
    sorted linked list without using extra space (in-place).
    Use a dummy head technique to simplify edge cases.
"""

print("=" * 60)
print("   ACTIVITY 1: Merge Two Sorted Linked Lists")
print("=" * 60)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        if values:
            for v in values:
                self.insert_at_end(v)

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def to_list(self):
        result, cur = [], self.head
        while cur:
            result.append(cur.data)
            cur = cur.next
        return result

    def display(self, label="List"):
        print(f"  {label}: {' -> '.join(map(str, self.to_list()))} -> NULL")


def merge_sorted_lists(head1, head2):
    """
    Merges two sorted linked lists.
    Returns the head of the merged sorted list.
    Time: O(m+n)  Space: O(1)
    """
    dummy = Node(0)           # sentinel/dummy node
    current = dummy

    a, b = head1, head2
    while a and b:
        if a.data <= b.data:
            current.next = a
            a = a.next
        else:
            current.next = b
            b = b.next
        current = current.next

    # Attach remaining nodes
    current.next = a if a else b
    return dummy.next


# ── Driver Code ──
list1 = LinkedList([1, 3, 5, 7, 9])
list2 = LinkedList([2, 4, 6, 8, 10])

print()
list1.display("List 1")
list2.display("List 2")

merged_head = merge_sorted_lists(list1.head, list2.head)
merged_ll = LinkedList()
merged_ll.head = merged_head
merged_ll.display("Merged ")

print("\n[+] Edge case — one empty list:")
empty = LinkedList()
list3 = LinkedList([5, 10, 15])
merged2 = merge_sorted_lists(empty.head, list3.head)
m2 = LinkedList(); m2.head = merged2
m2.display("Merged ")

print("\n[+] Edge case — both single elements:")
l4 = LinkedList([3])
l5 = LinkedList([1])
merged3 = merge_sorted_lists(l4.head, l5.head)
m3 = LinkedList(); m3.head = merged3
m3.display("Merged ")


# ──────────────────────────────────────────────────────────
#  ACTIVITY 2 — Detect and Remove Cycle (Floyd's Algorithm)
# ──────────────────────────────────────────────────────────
"""
Problem:
    (a) Detect if a linked list has a cycle using
        Floyd's Cycle Detection (tortoise & hare).
    (b) If cycle exists, find the node where cycle begins.
    (c) Remove the cycle to restore a proper linked list.
"""

print("\n" + "=" * 60)
print("   ACTIVITY 2: Detect & Remove Cycle — Floyd's Algo")
print("=" * 60)


def detect_cycle(head):
    """
    Returns (has_cycle: bool, meeting_node: Node | None)
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True, slow
    return False, None


def find_cycle_start(head, meeting_node):
    """
    After detection, move one pointer to head.
    Both pointers move 1 step at a time.
    They meet at the cycle start node.
    """
    ptr1 = head
    ptr2 = meeting_node
    while ptr1 is not ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    return ptr1   # cycle start node


def remove_cycle(head):
    """
    Detects cycle, finds its start, then removes it.
    Returns the corrected head.
    """
    has_cycle, meeting = detect_cycle(head)
    if not has_cycle:
        print("  [i] No cycle detected.")
        return head

    cycle_start = find_cycle_start(head, meeting)
    print(f"  [!] Cycle detected! Cycle starts at node with value: {cycle_start.data}")

    # Find the last node of the cycle (node whose .next == cycle_start)
    current = cycle_start
    while current.next is not cycle_start:
        current = current.next
    current.next = None   # break the cycle
    print(f"  [*] Cycle removed. Last node ({current.data}) now points to NULL.")
    return head


def list_to_display(head, max_nodes=20):
    """Safe display that stops after max_nodes (avoids infinite loop)."""
    elems, cur, count = [], head, 0
    while cur and count < max_nodes:
        elems.append(str(cur.data))
        cur = cur.next
        count += 1
    if cur:
        elems.append("...")
    return " -> ".join(elems) + " -> NULL"


# ── Build list with cycle: 1->2->3->4->5->3 (cycle at 3) ──
nodes = [Node(i) for i in [10, 20, 30, 40, 50]]
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]
nodes[-1].next = nodes[2]    # 50 -> 30 (cycle!)

print("\n[i] List with cycle (printed safely):")
print(" ", list_to_display(nodes[0]))

head = remove_cycle(nodes[0])

print("\n[i] List after removing cycle:")
print(" ", list_to_display(head))

# ── No cycle test ──
print("\n[+] Testing list WITHOUT cycle:")
normal = LinkedList([100, 200, 300])
remove_cycle(normal.head)


# ──────────────────────────────────────────────────────────
#  ACTIVITY 3 — Remove Duplicates & Find Intersection
# ──────────────────────────────────────────────────────────
"""
Problem:
    (a) Remove duplicates from a SORTED linked list — O(n).
    (b) Remove duplicates from an UNSORTED linked list
        using a hash set — O(n).
    (c) Find the intersection node of two linked lists
        using the length-difference technique — O(m+n).
"""

print("\n" + "=" * 60)
print("   ACTIVITY 3: Remove Duplicates & Find Intersection")
print("=" * 60)


# ── (a) Remove duplicates from SORTED list ──

def remove_duplicates_sorted(head):
    """
    In a sorted list, duplicates are adjacent.
    Skip nodes whose data equals the next node's data.
    Time: O(n)  Space: O(1)
    """
    current = head
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next   # skip duplicate
        else:
            current = current.next
    return head


print("\n[a] Remove duplicates from SORTED list:")
sorted_ll = LinkedList([1, 1, 2, 3, 3, 3, 4, 5, 5])
sorted_ll.display("Before")
remove_duplicates_sorted(sorted_ll.head)
sorted_ll.display("After ")


# ── (b) Remove duplicates from UNSORTED list ──

def remove_duplicates_unsorted(head):
    """
    Use a set to track seen values.
    If a value was already seen, skip that node.
    Time: O(n)  Space: O(n)
    """
    if not head:
        return head
    seen = {head.data}
    current = head
    while current.next:
        if current.next.data in seen:
            current.next = current.next.next    # skip duplicate
        else:
            seen.add(current.next.data)
            current = current.next
    return head


print("\n[b] Remove duplicates from UNSORTED list:")
unsorted_ll = LinkedList([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
unsorted_ll.display("Before")
remove_duplicates_unsorted(unsorted_ll.head)
unsorted_ll.display("After ")


# ── (c) Intersection of two linked lists ──

def get_length(head):
    length, cur = 0, head
    while cur:
        length += 1
        cur = cur.next
    return length


def find_intersection(head1, head2):
    """
    Align both lists to the same length, then walk together.
    The first common node is the intersection.
    Time: O(m+n)  Space: O(1)
    """
    len1 = get_length(head1)
    len2 = get_length(head2)

    a, b = head1, head2

    # Advance the longer list by the difference
    while len1 > len2:
        a = a.next
        len1 -= 1
    while len2 > len1:
        b = b.next
        len2 -= 1

    # Walk together until they meet
    while a and b:
        if a is b:
            return a
        a = a.next
        b = b.next
    return None


print("\n[c] Finding Intersection of two lists:")
# Build: listA = 1->2->3->  \
#                            6->7->NULL
# Build: listB = 4->5->  ---/
shared1 = Node(6)
shared2 = Node(7)
shared1.next = shared2

listA = LinkedList([1, 2, 3])
listB = LinkedList([4, 5])

# Manually attach shared nodes
cur = listA.head
while cur.next:
    cur = cur.next
cur.next = shared1

cur = listB.head
while cur.next:
    cur = cur.next
cur.next = shared1

listA.display("List A")
listB.display("List B")

intersection = find_intersection(listA.head, listB.head)
if intersection:
    print(f"  [*] Intersection at node with value: {intersection.data}")
else:
    print("  [*] No intersection found.")

print("\n[+] Testing non-intersecting lists:")
lx = LinkedList([1, 2, 3])
ly = LinkedList([7, 8, 9])
result = find_intersection(lx.head, ly.head)
print(f"  [*] Intersection: {'None' if not result else result.data}")
