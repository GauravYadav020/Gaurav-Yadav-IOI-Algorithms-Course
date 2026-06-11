# LESSON NAME: M13 Lesson 1 – Binary Search Tree

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Create an Inventory System for a bookstore using a BST.
# Each node represents a book ID. Implement insertion and display catalog.
# ==========================================
class BookNode:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.left = None
        self.right = None

class BookstoreBST:
    def __init__(self):
        self.root = None

    def insert(self, book_id, title):
        new_node = BookNode(book_id, title)
        if self.root is None:
            self.root = new_node
            print(f"Root Book added: {title} (ID: {book_id})")
            return
        current = self.root
        while True:
            if book_id < current.book_id:
                if current.left is None:
                    current.left = new_node
                    print(f"Added left: {title} (ID: {book_id})")
                    break
                current = current.left
            elif book_id > current.book_id:
                if current.right is None:
                    current.right = new_node
                    print(f"Added right: {title} (ID: {book_id})")
                    break
                current = current.right
            else:
                break

    def display_catalog(self, node):
        if node:
            self.display_catalog(node.left)
            print(f" -> [ID: {node.book_id}] Title: {node.title}")
            self.display_catalog(node.right)

print("--- Activity 1: Bookstore BST Catalog ---")
store = BookstoreBST()
store.insert(105, "Introduction to Python")
store.insert(102, "Data Structures 101")
store.insert(108, "Algorithms Made Easy")
store.display_catalog(store.root)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Build a Student Grade Tracker using a BST. Find min/max scores.
# ==========================================
class StudentNode:
    def __init__(self, score, name):
        self.score = score
        self.name = name
        self.left = self.right = None

class GradeTrackerBST:
    def __init__(self):
        self.root = None

    def insert(self, score, name):
        self.root = self._insert_recursive(self.root, score, name)

    def _insert_recursive(self, current, score, name):
        if current is None: return StudentNode(score, name)
        if score < current.score: current.left = self._insert_recursive(current.left, score, name)
        else: current.right = self._insert_recursive(current.right, score, name)
        return current

    def find_min(self, node):
        current = node
        while current and current.left is not None: current = current.left
        return current

print("\n--- Activity 2: Student Grade Tracker ---")
tracker = GradeTrackerBST()
tracker.insert(85, "Alice")
tracker.insert(72, "Bob")
lowest = tracker.find_min(tracker.root)
if lowest: print(f"Lowest Score: {lowest.name} ({lowest.score}%)")

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Automated Content Moderator using recursive BST keyword search.
# ==========================================
class KeywordNode:
    def __init__(self, word):
        self.word = word.lower()
        self.left = self.right = None

class ModerationTree:
    def __init__(self):
        self.root = None

    def add_keyword(self, word): self.root = self._add(self.root, word.lower())
    def _add(self, node, word):
        if not node: return KeywordNode(word)
        if word < node.word: node.left = self._add(node.left, word)
        elif word > node.word: node.right = self._add(node.right, word)
        return node
    def contains(self, node, word):
        if not node: return False
        if node.word == word.lower(): return True
        return self.contains(node.left, word) if word.lower() < node.word else self.contains(node.right, word)

print("\n--- Activity 3: AI Content Moderator ---")
moderator = ModerationTree()
moderator.add_keyword("scam")
print("Moderator initialized successfully.")