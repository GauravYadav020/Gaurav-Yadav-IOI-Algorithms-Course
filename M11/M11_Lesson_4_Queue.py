"""
M11 Lesson 4 – Queue
====================
Queue follows FIFO (First In, First Out) principle.
"""

class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0) if self.items else None
    
    def front(self):
        return self.items[0] if self.items else None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# Example
if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print("Front:", q.front())
    print("Dequeued:", q.dequeue())

"""
ACTIVITY 1: Implement Circular Queue
"""
class CircularQueue:
    def __init__(self, k):
        self.queue = [None] * k
        self.capacity = k
        self.head = 0
        self.tail = 0
        self.size = 0
    
    def enqueue(self, value):
        if self.size == self.capacity:
            return False
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
        return True

"""
ACTIVITY 2: Generate Binary Numbers from 1 to N using Queue
"""
from collections import deque

def generate_binary_numbers(n):
    q = deque()
    q.append("1")
    result = []
    for _ in range(n):
        num = q.popleft()
        result.append(num)
        q.append(num + "0")
        q.append(num + "1")
    return result

"""
ACTIVITY 3: Time needed to buy tickets (LeetCode style)
"""
def time_required_to_buy(tickets, k):
    q = deque()
    for i, t in enumerate(tickets):
        q.append((i, t))
    time = 0
    while q:
        person, ticket = q.popleft()
        time += 1
        if ticket > 1:
            q.append((person, ticket - 1))
        if person == k and ticket == 1:
            return time
    return time