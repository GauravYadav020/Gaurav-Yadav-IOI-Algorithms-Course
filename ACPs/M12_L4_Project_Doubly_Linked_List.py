# Module 12 Lesson 4: After-Class Project
# Project Name: Doubly Linked List Bi-Directional Node Pipeline Engine

class DoublyNode:
    def __init__(self, value):
        self.val = value
        self.next = self.prev = None

class DoublyLinkedListMatrix:
    def __init__(self): self.head = None
    def insert_node_tail(self, value):
        new_node = DoublyNode(value)
        if not self.head: self.head = new_node; return
        curr = self.head
        while curr.next: curr = curr.next
        curr.next = new_node
        new_node.prev = curr

if __name__ == "__main__":
    dll = DoublyLinkedListMatrix()
    dll.insert_node_tail(50); dll.insert_node_tail(100)
    print(f"Bi-directional chain tail trace: {dll.head.next.prev.val}")