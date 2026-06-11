"""
M11 Lesson 6 – Implementation of Stack using Queue
==================================================
Implement Stack using one or two Queues.
"""

from collections import deque

# Method 1: Stack using one Queue
class StackUsingQueue:
    def __init__(self):
        self.q = deque()
    
    def push(self, x):
        self.q.append(x)
        # Rotate the queue to bring new element to front
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
    
    def pop(self):
        return self.q.popleft() if self.q else None
    
    def top(self):
        return self.q[0] if self.q else None

# Method 2: Using two Queues (more efficient for pop)
class StackUsingTwoQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    
    def push(self, x):
        self.q1.append(x)
    
    def pop(self):
        if not self.q1: return None
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        popped = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return popped

"""
ACTIVITY 1: Implement Queue using Stack
"""
class QueueUsingStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self, x):
        self.stack1.append(x)
    
    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else None

"""
ACTIVITY 2: Design Circular Deque
"""
class MyCircularDeque:
    def __init__(self, k: int):
        self.queue = [0] * k
        self.front = 0
        self.rear = 0
        self.size = 0
        self.capacity = k

"""
ACTIVITY 3: Practice Problem - Valid Parentheses (Advanced)
"""
def is_valid(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return not stack

print("Activity 3 Test:")
print(is_valid("()[]{}"))  # True
print(is_valid("(]"))      # False