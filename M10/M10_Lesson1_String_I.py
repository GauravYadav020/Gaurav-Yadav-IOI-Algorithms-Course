"""
M10 Lesson 1 – String I
Advanced Python Implementation with 3 Activities
"""

def reverse_string(s):
    """Reverse a string using slicing (Pythonic way)"""
    return s[::-1]

def is_palindrome(s):
    """Check if string is palindrome (ignoring case and spaces)"""
    cleaned = ''.join(s.lower().split())
    return cleaned == cleaned[::-1]

def count_vowels(s):
    """Count vowels in a string"""
    vowels = set('aeiouAEIOU')
    return sum(1 for char in s if char in vowels)

# Activity 1: String Reversal with multiple methods
def activity1():
    print("=== Activity 1: String Reversal ===")
    text = "Hello World"
    print("Original:", text)
    print("Reversed (slicing):", reverse_string(text))
    print("Reversed (loop):", ''.join(reversed(text)))
    print("Reversed (two pointers):", two_pointer_reverse(text))

def two_pointer_reverse(s):
    """Reverse string using two pointers"""
    chars = list(s)
    left, right = 0, len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return ''.join(chars)

# Activity 2: Palindrome Checker
def activity2():
    print("\n=== Activity 2: Palindrome Checker ===")
    tests = ["radar", "A man a plan a canal Panama", "hello", "Was it a rat I saw"]
    for t in tests:
        print(f"'{t}' is palindrome: {is_palindrome(t)}")

# Activity 3: Advanced String Manipulation
def activity3():
    print("\n=== Activity 3: String Manipulation ===")
    s = "Python Programming"
    print("Original:", s)
    print("Vowels count:", count_vowels(s))
    print("Uppercase:", s.upper())
    print("Title case:", s.title())
    print("Words:", s.split())
    print("Replace 'o' with '0':", s.replace('o', '0'))

if __name__ == "__main__":
    print("M10 Lesson 1 – String Basics (I)")
    activity1()
    activity2()
    activity3()
    print("\n✅ All activities completed!")