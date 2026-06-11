# Module 11 Lesson 3: After-Class Project
# Project Name: Syntax Tree Compiler Token Balancer Validation Engine

def validate_syntax_enclosure(expression_string):
    mapping = {')': '(', '}': '{', ']': '['}
    stack = []
    for char in expression_string:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack.pop() != mapping[char]: return False
    return len(stack) == 0

if __name__ == "__main__":
    print(f"Is Code block structurally valid? {validate_syntax_enclosure('{[(x+y)*z]}')}")