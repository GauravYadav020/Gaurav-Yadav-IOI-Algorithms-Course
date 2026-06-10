# ============================================================
#        MODULE 9 - LESSON 1: LINKED LIST I
# ============================================================
# Topics Covered:
#   - Node creation and structure
#   - Singly Linked List: insertion (front, end, position)
#   - Traversal and display
#   - Search in linked list
# ============================================================


# ──────────────────────────────────────────────────────────
#  ACTIVITY 1 — Build a Linked List from Scratch
#              (Insert at Front, End, and by Position)
# ──────────────────────────────────────────────────────────
"""
Problem:
    Create a Node class and a LinkedList class.
    Support:
      - insert_at_front(data)
      - insert_at_end(data)
      - insert_at_position(pos, data)  [1-indexed]
      - display()
"""

print("=" * 60)
print("       ACTIVITY 1: Build & Insert in Linked List")
print("=" * 60)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # Insert at the beginning — O(1)
    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    # Insert at the end — O(n)
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.size += 1
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        self.size += 1

    # Insert at a given 1-indexed position — O(n)
    def insert_at_position(self, pos, data):
        if pos < 1 or pos > self.size + 1:
            print(f"  [!] Invalid position {pos}. Valid range: 1 to {self.size + 1}")
            return
        if pos == 1:
            self.insert_at_front(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(pos - 2):          # move to (pos-1)-th node
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.size += 1

    # Display the list as: data1 -> data2 -> ... -> NULL
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print("  List:", " -> ".join(elements) + " -> NULL" if elements else "NULL")

    def __len__(self):
        return self.size


# ── Driver Code ──
ll = LinkedList()

print("\n[+] Inserting at END: 10, 20, 30")
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.display()

print("\n[+] Inserting 5 at FRONT")
ll.insert_at_front(5)
ll.display()

print("\n[+] Inserting 15 at POSITION 3 (between 10 and 20)")
ll.insert_at_position(3, 15)
ll.display()

print("\n[+] Inserting 99 at POSITION 1 (new front)")
ll.insert_at_position(1, 99)
ll.display()

print("\n[+] Inserting 100 at POSITION beyond length (invalid)")
ll.insert_at_position(20, 100)

print(f"\n[i] Total nodes: {len(ll)}")


# ──────────────────────────────────────────────────────────
#  ACTIVITY 2 — Delete Nodes (Front, End, by Value)
# ──────────────────────────────────────────────────────────
"""
Problem:
    Extend the LinkedList class to support:
      - delete_from_front()
      - delete_from_end()
      - delete_by_value(val)   — removes FIRST occurrence
    After each deletion, display the updated list.
"""

print("\n" + "=" * 60)
print("       ACTIVITY 2: Delete from Linked List")
print("=" * 60)


class LinkedListV2(LinkedList):
    """Inherits LinkedList and adds deletion methods."""

    def delete_from_front(self):
        if self.head is None:
            print("  [!] List is empty, nothing to delete.")
            return None
        removed = self.head.data
        self.head = self.head.next
        self.size -= 1
        print(f"  [-] Deleted from front: {removed}")
        return removed

    def delete_from_end(self):
        if self.head is None:
            print("  [!] List is empty, nothing to delete.")
            return None
        # Only one node
        if self.head.next is None:
            removed = self.head.data
            self.head = None
            self.size -= 1
            print(f"  [-] Deleted from end: {removed}")
            return removed
        current = self.head
        while current.next.next:          # stop at second-to-last
            current = current.next
        removed = current.next.data
        current.next = None
        self.size -= 1
        print(f"  [-] Deleted from end: {removed}")
        return removed

    def delete_by_value(self, val):
        if self.head is None:
            print("  [!] List is empty.")
            return False
        # Value is at head
        if self.head.data == val:
            self.head = self.head.next
            self.size -= 1
            print(f"  [-] Deleted node with value: {val}")
            return True
        current = self.head
        while current.next:
            if current.next.data == val:
                current.next = current.next.next
                self.size -= 1
                print(f"  [-] Deleted node with value: {val}")
                return True
            current = current.next
        print(f"  [!] Value {val} not found in list.")
        return False


# ── Driver Code ──
ll2 = LinkedListV2()
for val in [10, 20, 30, 40, 50]:
    ll2.insert_at_end(val)

print("\n[i] Initial list:")
ll2.display()

print("\n[+] Delete from FRONT:")
ll2.delete_from_front()
ll2.display()

print("\n[+] Delete from END:")
ll2.delete_from_end()
ll2.display()

print("\n[+] Delete by VALUE 30:")
ll2.delete_by_value(30)
ll2.display()

print("\n[+] Delete by VALUE 99 (not in list):")
ll2.delete_by_value(99)
ll2.display()

print(f"\n[i] Remaining nodes: {len(ll2)}")


# ──────────────────────────────────────────────────────────
#  ACTIVITY 3 — Reverse a Linked List + Detect Middle Node
# ──────────────────────────────────────────────────────────
"""
Problem:
    (a) Reverse a singly linked list in-place using the
        iterative three-pointer technique.
    (b) Find the middle node using the slow-fast (tortoise
        and hare) pointer technique.
    (c) Count occurrences of a given value.
"""

print("\n" + "=" * 60)
print("  ACTIVITY 3: Reverse, Find Middle & Count Occurrences")
print("=" * 60)


class LinkedListV3(LinkedListV2):

    # Reverse in-place — O(n) time, O(1) space
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next   # save next
            current.next = prev        # reverse pointer
            prev = current             # move prev forward
            current = next_node        # move current forward
        self.head = prev
        print("  [*] List reversed.")

    # Find middle node using slow-fast pointer — O(n)
    def find_middle(self):
        if self.head is None:
            print("  [!] List is empty.")
            return None
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next           # moves 1 step
            fast = fast.next.next     # moves 2 steps
        print(f"  [*] Middle node value: {slow.data}")
        return slow.data

    # Count occurrences of a value — O(n)
    def count_occurrences(self, val):
        count = 0
        current = self.head
        while current:
            if current.data == val:
                count += 1
            current = current.next
        print(f"  [*] Occurrences of {val}: {count}")
        return count


# ── Driver Code ──
ll3 = LinkedListV3()
for val in [1, 2, 3, 2, 4, 2, 5]:
    ll3.insert_at_end(val)

print("\n[i] Initial list:")
ll3.display()

print("\n[+] Finding middle node:")
ll3.find_middle()

print("\n[+] Counting occurrences of 2:")
ll3.count_occurrences(2)

print("\n[+] Reversing the list:")
ll3.reverse()
ll3.display()

print("\n[+] Finding middle of reversed list:")
ll3.find_middle()

print("\n[+] Edge case — single element list:")
single = LinkedListV3()
single.insert_at_end(42)
single.display()
single.find_middle()
single.reverse()
single.display()
