# LESSON NAME: M13 Lesson 6 – B Trees and B+ Trees

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Multi-way indexing capacity layout inspector setup configuration engine.
# ==========================================
class BTreeNodeLayout:
    def __init__(self, degree, is_leaf=True):
        self.degree = degree
        self.is_leaf = is_leaf
        self.keys = []
        self.children = []
    def inspect(self):
        print(f"Node Info -> Is Leaf: {self.is_leaf}, Current Keys Loaded: {len(self.keys)}")

print("--- Activity 1: Node Layout Constructor ---")
node = BTreeNodeLayout(degree=3)
node.keys = [10, 20]
node.inspect()

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: B-Tree internal node traversal lookup and multi-branch structural mapping router.
# ==========================================
class BTreeNode:
    def __init__(self, t, leaf=True):
        self.keys = []
        self.children = []
        self.leaf = leaf

class BTreeSearchEngine:
    def __init__(self, degree): self.root = BTreeNode(degree)
    def search_node(self, node, key):
        i = 0
        while i < len(node.keys) and key > node.keys[i]: i += 1
        if i < len(node.keys) and node.keys[i] == key: return True
        if node.leaf: return False
        return self.search_node(node.children[i], key)

print("\n--- Activity 2: B-Tree Path Search Navigation ---")
engine = BTreeSearchEngine(2)
engine.root.keys = [30]
print(f"Search status for key (30): {engine.search_node(engine.root, 30)}")

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Database file storage system simulation utilizing sequential linked leaf layout.
# ==========================================
class BPlusLeafNode:
    def __init__(self):
        self.keys = []
        self.values = []
        self.next_leaf_pointer = None

class SimplifiedBPlusTreeStorage:
    def __init__(self):
        self.leaf_1 = BPlusLeafNode()
        self.leaf_2 = BPlusLeafNode()
        self.leaf_1.keys = [10, 25]
        self.leaf_1.values = ["Record_A", "Record_B"]
        self.leaf_1.next_leaf_pointer = self.leaf_2
    def sequential_scan(self):
        curr = self.leaf_1
        while curr:
            print(f"Leaf Keys Block: {curr.keys} -> Record Mapping: {curr.values}")
            curr = curr.next_leaf_pointer

print("\n--- Activity 3: B+ Tree Sequential Tablespace Scan ---")
db = SimplifiedBPlusTreeStorage()
db.sequential_scan()