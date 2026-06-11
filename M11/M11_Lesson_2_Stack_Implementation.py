"""
M11 Lesson 2 – Stack Implementation
===================================
Different ways to implement Stack: Using List, Linked List, etc.
"""

# 1. Stack using Python List (already efficient)
class StackList:
    def __init__(self):
        self.items = []
    
    def push(self, item): self.items.append(item)
    def pop(self): return self.items.pop() if self.items else None
    def peek(self): return self.items[-1] if self.items else None

# 2. Stack using Linked List (more memory efficient for large data)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
    
    def pop(self):
        if self.top is None:
            return None
        popped = self.top.data
        self.top = self.top.next
        self.size -= 1
        return popped

"""
ACTIVITY 1: Implement Stack with fixed size (Array based)
"""
class FixedStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.top = -1
    
    def push(self, item):
        if self.top >= self.capacity - 1:
            print("Stack Overflow!")
            return False
        self.top += 1
        self.items[self.top] = item
        return True

"""
ACTIVITY 2: Undo functionality using Stack
"""
class UndoManager:
    def __init__(self):
        self.history = StackList()
    
    def do_action(self, action):
        self.history.push(action)
        print(f"Performed: {action}")
    
    def undo(self):
        if not self.history.peek():
            print("Nothing to undo")
            return
        last_action = self.history.pop()
        print(f"Undid: {last_action}")

"""
ACTIVITY 3: Infix to Postfix conversion using Stack
"""
def infix_to_postfix(expression):
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    stack = StackList()
    postfix = []
    
    for char in expression:
        if char.isalnum():
            postfix.append(char)
        elif char in precedence:
            while stack.peek() and precedence.get(stack.peek(), 0) >= precedence[char]:
                postfix.append(stack.pop())
            stack.push(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while stack.peek() and stack.peek() != '(':
                postfix.append(stack.pop())
            stack.pop()  # remove '('
    
    while stack.peek():
        postfix.append(stack.pop())
    return ''.join(postfix)

print("Activity 3 - Infix to Postfix:")
print(infix_to_postfix("A+B*C"))