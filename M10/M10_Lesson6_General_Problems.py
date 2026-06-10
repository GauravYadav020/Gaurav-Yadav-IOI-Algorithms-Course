"""
M10 Lesson 6 – General String Problems
Common Interview Problems
"""

def group_anagrams(strs):
    """Group Anagrams"""
    from collections import defaultdict
    groups = defaultdict(list)
    for s in strs:
        groups[tuple(sorted(s))].append(s)
    return list(groups.values())

def longest_palindromic_substring(s):
    """Longest Palindromic Substring (Expand Around Center)"""
    if not s:
        return ""
    start = 0
    max_len = 1
    for i in range(len(s)):
        # Odd length
        left = right = i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > max_len:
                start = left
                max_len = right - left + 1
            left -= 1
            right += 1
        # Even length
        left = i
        right = i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > max_len:
                start = left
                max_len = right - left + 1
            left -= 1
            right += 1
    return s[start:start + max_len]

def valid_parentheses(s):
    """Check valid parentheses"""
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

# Activity 1: Group Anagrams
def activity1():
    print("=== Activity 1: Group Anagrams ===")
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(strs)
    print("Groups:", result)

# Activity 2: Longest Palindrome
def activity2():
    print("\n=== Activity 2: Longest Palindromic Substring ===")
    tests = ["babad", "cbbd", "a"]
    for t in tests:
        print(f"'{t}' -> '{longest_palindromic_substring(t)}'")

# Activity 3: Valid Parentheses & More
def activity3():
    print("\n=== Activity 3: Valid Parentheses ===")
    tests = ["()", "()[]{}", "(]", "([)]"]
    for t in tests:
        print(f"'{t}' is valid: {valid_parentheses(t)}")

if __name__ == "__main__":
    print("M10 Lesson 6 – General String Problems")
    activity1()
    activity2()
    activity3()
    print("\n✅ General Problems Activities Completed!")