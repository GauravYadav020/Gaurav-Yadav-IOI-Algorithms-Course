# Module 12 Lesson 1: After-Class Project
# Project Name: Singly Linked List Data Storage Inversion Engine

class Node:
    def __init__(self, data_val):
        self.data = data_val
        self.next = None

class SinglyLinkedListCollection:
    def __init__(self): self.head = None
    def append(self, val):
        if not self.head: self.head = Node(val); return
        curr = self.head
        while curr.next: curr = curr.next
        curr.next = Node(val)
    def reverse_list_inplace(self):
        prev, curr = None, self.head
        while curr:
            next_step = curr.next
            curr.next = prev
            prev = curr
            curr = next_step
        self.head = prev

if __name__ == "__main__":
    sll = SinglyLinkedListCollection()
    sll.append(1); sll.append(2); sll.append(3)
    sll.reverse_list_inplace()
    print(f"Head of reversed framework link structure: {sll.head.data}")