"""
M11 Lesson 3 – Double Stack
===========================
Two stacks in one array or efficient use of two stacks.
"""

# Two Stacks in one Array
class TwoStacks:
    def __init__(self, n):
        self.size = n
        self.arr = [None] * n
        self.top1 = -1
        self.top2 = n
    
    def push1(self, x):
        if self.top1 + 1 == self.top2:
            print("Stack 1 Overflow")
            return
        self.top1 += 1
        self.arr[self.top1] = x
    
    def push2(self, x):
        if self.top1 + 1 == self.top2:
            print("Stack 2 Overflow")
            return
        self.top2 -= 1
        self.arr[self.top2] = x
    
    def pop1(self):
        if self.top1 == -1: return None
        x = self.arr[self.top1]
        self.top1 -= 1
        return x
    
    def pop2(self):
        if self.top2 == self.size: return None
        x = self.arr[self.top2]
        self.top2 += 1
        return x

"""
ACTIVITY 1: Sort a stack using temporary stack
"""
def sort_stack(stack):
    tmp_stack = StackList()  # from previous lesson
    while stack:
        tmp = stack.pop()
        while tmp_stack and tmp_stack.peek() > tmp:
            stack.push(tmp_stack.pop())
        tmp_stack.push(tmp)
    return tmp_stack

"""
ACTIVITY 2: Evaluate Postfix expression using Stack
"""
def evaluate_postfix(postfix):
    stack = StackList()
    for char in postfix:
        if char.isdigit():
            stack.push(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            if char == '+': stack.push(a + b)
            elif char == '-': stack.push(a - b)
            elif char == '*': stack.push(a * b)
            elif char == '/': stack.push(a // b)
    return stack.pop()

"""
ACTIVITY 3: Next Greater Element using Stack
"""
def next_greater_element(arr):
    stack = StackList()
    result = [-1] * len(arr)
    for i in range(len(arr)-1, -1, -1):
        while stack and stack.peek() <= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack.peek()
        stack.push(arr[i])
    return result

print("Activity 3 Example:")
print(next_greater_element([4, 5, 2, 25]))