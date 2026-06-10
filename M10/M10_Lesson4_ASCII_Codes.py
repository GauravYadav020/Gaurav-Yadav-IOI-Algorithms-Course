"""
M10 Lesson 4 – ASCII Codes
Working with Character Codes
"""

def char_to_ascii(c):
    """Convert character to ASCII value"""
    return ord(c)

def ascii_to_char(n):
    """Convert ASCII value to character"""
    return chr(n)

def caesar_cipher(text, shift):
    """Simple Caesar Cipher"""
    result = ""
    for char in text:
        if char.isalpha():
            ascii_val = ord(char)
            if char.isupper():
                result += chr((ascii_val - 65 + shift) % 26 + 65)
            else:
                result += chr((ascii_val - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

# Activity 1: ASCII Exploration
def activity1():
    print("=== Activity 1: ASCII Values ===")
    for c in "ABCabc123":
        print(f"'{c}' -> ASCII: {char_to_ascii(c)}")

# Activity 2: Caesar Cipher Encryption
def activity2():
    print("\n=== Activity 2: Caesar Cipher ===")
    message = "Hello World"
    encrypted = caesar_cipher(message, 3)
    decrypted = caesar_cipher(encrypted, -3)
    print("Original:", message)
    print("Encrypted (+3):", encrypted)
    print("Decrypted:", decrypted)

# Activity 3: ASCII Art Generator
def activity3():
    print("\n=== Activity 3: Simple ASCII Art ===")
    text = "HI"
    for line in range(5):
        print(''.join(chr(ord(c) + line) if c.isalpha() else c for c in text))

if __name__ == "__main__":
    print("M10 Lesson 4 – ASCII Codes")
    activity1()
    activity2()
    activity3()
    print("\n✅ ASCII Activities Completed!")