"""
M11 Lesson 1 – Stack
========================
A Stack is a linear data structure that follows LIFO (Last In, First Out) principle.
"""

# Basic Stack using List
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add item to the top of the stack"""
        self.items.append(item)
        print(f"Pushed {item} to stack")
    
    def pop(self):
        """Remove and return item from the top"""
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty!"
    
    def peek(self):
        """Return top item without removing"""
        if not self.is_empty():
            return self.items[-1]
        return "Stack is empty!"
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# Example Usage
if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    print("Top element:", s.peek())
    print("Popped:", s.pop())
    print("Stack size:", s.size())

"""
ACTIVITY 1: Reverse a string using Stack
"""
def reverse_string(text):
    stack = Stack()
    for char in text:
        stack.push(char)
    reversed_text = ""
    while not stack.is_empty():
        reversed_text += stack.pop()
    return reversed_text

print("\nActivity 1 - Reverse String:")
print(reverse_string("Hello World"))

"""
ACTIVITY 2: Check balanced parentheses
"""
def is_balanced(expression):
    stack = Stack()
    brackets = {')': '(', '}': '{', ']': '['}
    for char in expression:
        if char in '({[':
            stack.push(char)
        elif char in ')}]':
            if stack.is_empty() or stack.pop() != brackets[char]:
                return False
    return stack.is_empty()

print("\nActivity 2 - Balanced Parentheses:")
print(is_balanced("({[]})"))  # True
print(is_balanced("({[})"))   # False

"""
ACTIVITY 3: Implement stack with max operation
"""
class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []
    
    def push(self, x):
        self.stack.append(x)
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)
    
    def pop(self):
        if self.stack:
            x = self.stack.pop()
            if x == self.max_stack[-1]:
                self.max_stack.pop()
            return x
        return None
    
    def get_max(self):
        return self.max_stack[-1] if self.max_stack else None

print("\nActivity 3 - MaxStack Example:")
ms = MaxStack()
ms.push(5)
ms.push(1)
ms.push(7)
print("Max:", ms.get_max())