# LESSON NAME: M13 Lesson 2 – Operations on a Binary Search Tree

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Smart-home temperature tracker. Average temp computation.
# ==========================================
class TempNode:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None

class ClimateTracker:
    def __init__(self): self.root = None
    def insert(self, val):
        if not self.root: self.root = TempNode(val); return
        curr = self.root
        while True:
            if val < curr.value:
                if not curr.left: curr.left = TempNode(val); break
                curr = curr.left
            else:
                if not curr.right: curr.right = TempNode(val); break
                curr = curr.right
    def compute_stats(self, node, data_list=[]):
        if node:
            self.compute_stats(node.left, data_list)
            data_list.append(node.value)
            self.compute_stats(node.right, data_list)
        return data_list

print("--- Activity 1: Smart Climate Tracker ---")
tracker = ClimateTracker()
for r in [22.5, 19.0, 26.4]: tracker.insert(r)
print(f"Readings: {tracker.compute_stats(tracker.root, [])}")

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Bank Audit Level-Order Traversal (BFS) system.
# ==========================================
class AccountNode:
    def __init__(self, balance, owner):
        self.balance = balance
        self.owner = owner
        self.left = self.right = None

class BankAuditBST:
    def __init__(self): self.root = None
    def insert(self, balance, owner):
        def _insert(node):
            if not node: return AccountNode(balance, owner)
            if balance < node.balance: node.left = _insert(node.left)
            else: node.right = _insert(node.right)
            return node
        self.root = _insert(self.root)
    def print_level_order(self):
        if not self.root: return
        queue = [self.root]
        while queue:
            curr = queue.pop(0)
            print(f"[{curr.owner}: ${curr.balance}] ", end="")
            if curr.left: queue.append(curr.left)
            if curr.right: queue.append(curr.right)
        print()

print("\n--- Activity 2: Level-Order Bank Audit ---")
bank = BankAuditBST()
bank.insert(50000, "Corporate")
bank.print_level_order()

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: OS Database Validation and Tree Inversion (Mirroring).
# ==========================================
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class TreeValidatorEngine:
    def is_valid_bst(self, root, low=float('-inf'), high=float('inf')):
        if not root: return True
        if not (low < root.val < high): return False
        return self.is_valid_bst(root.left, low, root.val) and self.is_valid_bst(root.right, root.val, high)

print("\n--- Activity 3: Integrity Validation ---")
engine = TreeValidatorEngine()
root = TreeNode(50)
print(f"Is valid BST? {engine.is_valid_bst(root)}")