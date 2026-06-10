"""
M10 Lesson 3 – Playing with frequencies
Character Frequency Analysis
"""

from collections import Counter

def frequency_dict(s):
    """Return frequency of each character"""
    return dict(Counter(s))

def most_frequent_char(s):
    """Find most frequent character"""
    if not s:
        return None
    return Counter(s).most_common(1)[0]

def frequency_sort(s):
    """Sort string by character frequency"""
    freq = Counter(s)
    return ''.join(sorted(s, key=lambda x: (-freq[x], x)))

# Activity 1: Basic Frequency Count
def activity1():
    print("=== Activity 1: Character Frequency ===")
    text = "hello world"
    freq = frequency_dict(text)
    print("Frequencies:", freq)
    for char, count in sorted(freq.items()):
        print(f"'{char}': {count}")

# Activity 2: Most Frequent Character
def activity2():
    print("\n=== Activity 2: Most Frequent Characters ===")
    texts = ["mississippi", "banana", "aabbcc"]
    for t in texts:
        char, count = most_frequent_char(t)
        print(f"In '{t}' -> '{char}' appears {count} times")

# Activity 3: Frequency-based Sorting
def activity3():
    print("\n=== Activity 3: Frequency Sort ===")
    s = "tree"
    print("Original:", s)
    print("Sorted by frequency:", frequency_sort(s))

if __name__ == "__main__":
    print("M10 Lesson 3 – Playing with Frequencies")
    activity1()
    activity2()
    activity3()
    print("\n✅ Frequency Activities Completed!")