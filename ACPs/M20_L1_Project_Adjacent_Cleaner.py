# Module 20 Lesson 1: After-Class Project
# Project Name: Competitive String Token Multi-Pass Reduction Pipeline

def eliminate_matching_adjacent_characters(raw_string):
    stack = []
    for char in raw_string:
        if stack and stack[-1] == char: stack.pop()
        else: stack.append(char)
    return "".join(stack)

if __name__ == "__main__":
    print(f"Processed String Optimization Cleared Vector: '{eliminate_matching_adjacent_characters('abbaay')}'")