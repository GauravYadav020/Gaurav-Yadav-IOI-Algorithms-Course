"""
M10 Lesson 2 – String II
Advanced String Operations
"""

def anagram_check(s1, s2):
    """Check if two strings are anagrams"""
    return sorted(s1.lower()) == sorted(s2.lower())

def longest_substring_no_repeat(s):
    """Find length of longest substring without repeating characters"""
    char_set = set()
    left = 0
    max_length = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length

def string_compression(s):
    """Compress string like 'aaabbcc' -> 'a3b2c2'"""
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result.append(s[i-1] + str(count))
            count = 1
    result.append(s[-1] + str(count))
    return ''.join(result)

# Activity 1: Anagram Checker
def activity1():
    print("=== Activity 1: Anagram Checker ===")
    pairs = [("listen", "silent"), ("hello", "world"), ("rat", "tar")]
    for a, b in pairs:
        print(f"'{a}' and '{b}' are anagrams: {anagram_check(a, b)}")

# Activity 2: Longest Unique Substring
def activity2():
    print("\n=== Activity 2: Longest Substring Without Repeating Characters ===")
    tests = ["abcabcbb", "bbbbb", "pwwkew", "dvdf"]
    for t in tests:
        print(f"'{t}' -> Length: {longest_substring_no_repeat(t)}")

# Activity 3: String Compression & Decompression
def activity3():
    print("\n=== Activity 3: String Compression ===")
    s = "aabcccccaaa"
    compressed = string_compression(s)
    print("Original:", s)
    print("Compressed:", compressed)

if __name__ == "__main__":
    print("M10 Lesson 2 – Advanced Strings (II)")
    activity1()
    activity2()
    activity3()
    print("\n✅ Lesson 2 Activities Completed!")