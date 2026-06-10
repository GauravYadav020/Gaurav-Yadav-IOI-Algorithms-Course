"""
M10 Lesson 5 – String Algorithms
KMP, Rabin-Karp, etc.
"""

def kmp_search(text, pattern):
    """Knuth-Morris-Pratt string search"""
    if not pattern:
        return 0
    lps = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == len(pattern):
            return i - j
        elif i < len(text) and text[i] != pattern[j]:
            j = lps[j-1] if j > 0 else 0
            i += 1
    return -1

def rabin_karp(text, pattern):
    """Rabin-Karp algorithm"""
    if len(pattern) > len(text):
        return -1
    d = 256
    q = 101
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1
    for i in range(m-1):
        h = (h * d) % q
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(n - m + 1):
        if p == t:
            if text[i:i+m] == pattern:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i+m])) % q
            if t < 0:
                t += q
    return -1

# Activity 1: KMP Search
def activity1():
    print("=== Activity 1: KMP Pattern Search ===")
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    pos = kmp_search(text, pattern)
    print(f"Pattern '{pattern}' found at index: {pos}")

# Activity 2: Rabin-Karp
def activity2():
    print("\n=== Activity 2: Rabin-Karp ===")
    text = "GEEKS FOR GEEKS"
    pattern = "GEEKS"
    pos = rabin_karp(text, pattern)
    print(f"Pattern '{pattern}' found at index: {pos}")

# Activity 3: Multiple Pattern Search
def activity3():
    print("\n=== Activity 3: Multiple Algorithms Comparison ===")
    text = "This is a test string for searching"
    patterns = ["test", "string", "for"]
    for p in patterns:
        print(f"KMP for '{p}': {kmp_search(text, p)}")
        print(f"Rabin-Karp for '{p}': {rabin_karp(text, p)}")

if __name__ == "__main__":
    print("M10 Lesson 5 – String Algorithms")
    activity1()
    activity2()
    activity3()
    print("\n✅ Algorithm Activities Completed!")