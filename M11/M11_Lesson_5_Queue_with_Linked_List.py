"""
M11 Lesson 5 – Queue with Linked List
=====================================
Efficient Queue using Linked List (O(1) enqueue and dequeue)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.length += 1
    
    def dequeue(self):
        if self.front is None:
            return None
        temp = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.length -= 1
        return temp

"""
ACTIVITY 1: Implement Deque (Double Ended Queue) using Linked List
"""
class DequeNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

"""
ACTIVITY 2: First Non-Repeating Character in Stream
"""
from collections import deque, Counter

def first_non_repeating(stream):
    q = deque()
    count = Counter()
    result = []
    for char in stream:
        count[char] += 1
        q.append(char)
        while q and count[q[0]] > 1:
            q.popleft()
        result.append(q[0] if q else -1)
    return result

"""
ACTIVITY 3: Sliding Window Maximum using Deque
"""
from collections import deque

def max_sliding_window(nums, k):
    if not nums: return []
    dq = deque()
    result = []
    for i in range(len(nums)):
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)
        if dq[0] == i - k:
            dq.popleft()
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result

print("Activity 3 Example:")
print(max_sliding_window([1,3,-1,-3,5,3,6,7], 3))