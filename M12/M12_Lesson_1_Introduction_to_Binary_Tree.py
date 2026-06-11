"""
M12 Lesson 1 – Introduction to Binary Tree

A Binary Tree is a hierarchical data structure where each node has at most two children.
- Root: Topmost node
- Parent, Child, Leaf nodes
"""

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

# Example: Creating a simple binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Binary Tree created successfully!")
print(f"Root: {root.val}")

# Activity 1: Create a binary tree with 7 nodes
def create_sample_tree():
    root = TreeNode(10)
    root.left = TreeNode(20)
    root.right = TreeNode(30)
    root.left.left = TreeNode(40)
    root.left.right = TreeNode(50)
    root.right.left = TreeNode(60)
    root.right.right = TreeNode(70)
    return root

# Activity 2: Count number of nodes (simple recursive)
def count_nodes(root):
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

# Activity 3: Check if a value exists in the tree
def search_value(root, target):
    if not root:
        return False
    if root.val == target:
        return True
    return search_value(root.left, target) or search_value(root.right, target)

# Test Activities
tree = create_sample_tree()
print("Total nodes:", count_nodes(tree))
print("Is 50 present?", search_value(tree, 50))
print("Is 100 present?", search_value(tree, 100))
