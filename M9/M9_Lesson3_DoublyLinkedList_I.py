# ============================================================
#        MODULE 9 - LESSON 3: DOUBLY LINKED LIST I
# ============================================================
# Topics Covered:
#   - DLL Node structure (prev + next pointers)
#   - Insert at front, end, and specific position
#   - Forward and backward traversal
#   - Delete from front, end, and by value
# ============================================================


# ──────────────────────────────────────────────────────────
#  ACTIVITY 1 — Build a Doubly Linked List (Insert & Display)
# ──────────────────────────────────────────────────────────
"""
Problem:
    Create a DLLNode class with prev and next pointers.
    Implement DoublyLinkedList supporting:
      - insert_at_front(data)
      - insert_at_end(data)
      - insert_at_position(pos, data)  [1-indexed]
      - display_forward()
      - display_backward()
"""

print("=" * 60)
print("   ACTIVITY 1: Build Doubly Linked List — Insert & Display")
print("=" * 60)


class DLLNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __repr__(self):
        return f"DLLNode({self.data})"


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_at_front(self, data):
        new_node = DLLNode(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def insert_at_end(self, data):
        new_node = DLLNode(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def insert_at_position(self, pos, data):
        """1-indexed position insert."""
        if pos < 1 or pos > self.size + 1:
            print(f"  [!] Invalid position {pos}. Valid: 1 to {self.size + 1}")
            return
        if pos == 1:
            self.insert_at_front(data)
            return
        if pos == self.size + 1:
            self.insert_at_end(data)
            return

        new_node = DLLNode(data)
        current = self.head
        for _ in range(pos - 2):
            current = current.next   # reach (pos-1)-th node

        next_node = current.next
        new_node.prev = current
        new_node.next = next_node
        current.next = new_node
        if next_node:
            next_node.prev = new_node
        self.size += 1

    def display_forward(self):
        """Traverse head → tail."""
        elems = []
        current = self.head
        while current:
            elems.append(str(current.data))
            current = current.next
        arrow = " <-> ".join(elems)
        print(f"  Forward : NULL <-> {arrow} <-> NULL" if elems else "  Forward : NULL")

    def display_backward(self):
        """Traverse tail → head using prev pointers."""
        elems = []
        current = self.tail
        while current:
            elems.append(str(current.data))
            current = current.prev
        arrow = " <-> ".join(elems)
        print(f"  Backward: NULL <-> {arrow} <-> NULL" if elems else "  Backward: NULL")

    def __len__(self):
        return self.size


# ── Driver Code ──
dll = DoublyLinkedList()

print("\n[+] Inserting at END: 10, 20, 30, 40")
for val in [10, 20, 30, 40]:
    dll.insert_at_end(val)
dll.display_forward()
dll.display_backward()

print("\n[+] Inserting 5 at FRONT:")
dll.insert_at_front(5)
dll.display_forward()

print("\n[+] Inserting 25 at POSITION 4 (between 20 and 30):")
dll.insert_at_position(4, 25)
dll.display_forward()
dll.display_backward()

print(f"\n[i] Total nodes: {len(dll)}")

print("\n[+] Inserting at invalid position 100:")
dll.insert_at_position(100, 999)


# ──────────────────────────────────────────────────────────
#  ACTIVITY 2 — Delete from a Doubly Linked List
# ──────────────────────────────────────────────────────────
"""
Problem:
    Add deletion operations to the DLL:
      - delete_from_front()
      - delete_from_end()
      - delete_by_value(val)
    Maintain prev/next links correctly on every deletion.
"""

print("\n" + "=" * 60)
print("   ACTIVITY 2: Delete from Doubly Linked List")
print("=" * 60)


class DoublyLinkedListV2(DoublyLinkedList):

    def delete_from_front(self):
        if not self.head:
            print("  [!] List is empty.")
            return None
        removed = self.head.data
        if self.head is self.tail:            # single node
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        print(f"  [-] Deleted from front: {removed}")
        return removed

    def delete_from_end(self):
        if not self.tail:
            print("  [!] List is empty.")
            return None
        removed = self.tail.data
        if self.head is self.tail:            # single node
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        print(f"  [-] Deleted from end: {removed}")
        return removed

    def delete_by_value(self, val):
        current = self.head
        while current:
            if current.data == val:
                if current is self.head:
                    self.delete_from_front()
                elif current is self.tail:
                    self.delete_from_end()
                else:
                    # Bypass current node
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    self.size -= 1
                    print(f"  [-] Deleted node with value: {val}")
                return True
            current = current.next
        print(f"  [!] Value {val} not found.")
        return False


# ── Driver Code ──
dll2 = DoublyLinkedListV2()
for val in [10, 20, 30, 40, 50]:
    dll2.insert_at_end(val)

print("\n[i] Initial list:")
dll2.display_forward()

print("\n[+] Delete from FRONT:")
dll2.delete_from_front()
dll2.display_forward()

print("\n[+] Delete from END:")
dll2.delete_from_end()
dll2.display_forward()

print("\n[+] Delete by VALUE 30 (middle node):")
dll2.delete_by_value(30)
dll2.display_forward()
dll2.display_backward()

print(f"\n[i] Remaining nodes: {len(dll2)}")

print("\n[+] Delete all remaining nodes one by one from FRONT:")
while dll2.head:
    dll2.delete_from_front()
dll2.display_forward()

print("\n[+] Delete from empty list:")
dll2.delete_from_end()


# ──────────────────────────────────────────────────────────
#  ACTIVITY 3 — Reverse a DLL + Sort using Bubble Sort
# ──────────────────────────────────────────────────────────
"""
Problem:
    (a) Reverse a doubly linked list by swapping
        prev and next pointers of every node — O(n).
    (b) Sort a doubly linked list using Bubble Sort
        by swapping data values between adjacent nodes — O(n²).
    (c) Check if the DLL is a palindrome — O(n).
"""

print("\n" + "=" * 60)
print("   ACTIVITY 3: Reverse, Sort & Palindrome Check on DLL")
print("=" * 60)


class DoublyLinkedListV3(DoublyLinkedListV2):

    def reverse(self):
        """
        Swap prev and next for every node.
        Move head to what was the tail.
        Time: O(n)  Space: O(1)
        """
        current = self.head
        new_head = None
        while current:
            # Swap prev and next
            current.prev, current.next = current.next, current.prev
            new_head = current
            current = current.prev   # move to old next (now prev after swap)
        self.head, self.tail = new_head, self.head
        print("  [*] DLL reversed.")

    def bubble_sort(self):
        """
        Repeatedly compare adjacent node data and swap if needed.
        Time: O(n²)  Space: O(1)
        """
        if not self.head:
            return
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next
        print("  [*] DLL sorted using Bubble Sort.")

    def is_palindrome(self):
        """
        Use two pointers: left (head→) and right (tail←).
        Compare until they meet in the middle.
        Time: O(n)  Space: O(1)
        """
        left = self.head
        right = self.tail
        length = self.size

        for _ in range(length // 2):
            if left.data != right.data:
                print(f"  [*] NOT a palindrome (mismatch: {left.data} vs {right.data})")
                return False
            left = left.next
            right = right.prev
        print("  [*] IS a palindrome!")
        return True


# ── Driver Code ──
dll3 = DoublyLinkedListV3()
for val in [5, 3, 1, 4, 2]:
    dll3.insert_at_end(val)

print("\n[i] Original list:")
dll3.display_forward()

print("\n[+] Bubble Sort:")
dll3.bubble_sort()
dll3.display_forward()

print("\n[+] Reversing sorted list:")
dll3.reverse()
dll3.display_forward()
dll3.display_backward()

print("\n[+] Palindrome check on: 1 2 3 2 1")
pal = DoublyLinkedListV3()
for v in [1, 2, 3, 2, 1]:
    pal.insert_at_end(v)
pal.display_forward()
pal.is_palindrome()

print("\n[+] Palindrome check on: 1 2 3 4 5")
non_pal = DoublyLinkedListV3()
for v in [1, 2, 3, 4, 5]:
    non_pal.insert_at_end(v)
non_pal.display_forward()
non_pal.is_palindrome()
