"""
M12 Lesson 2 – Operations on Binary Tree

Common operations: Insert, Delete, Find Height, etc.
"""

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

# Activity 1: Insert into Binary Tree (level order insertion)
from collections import deque

def insert_into_tree(root, value):
    if not root:
        return TreeNode(value)
    q = deque([root])
    while q:
        node = q.popleft()
        if not node.left:
            node.left = TreeNode(value)
            return root
        else:
            q.append(node.left)
        if not node.right:
            node.right = TreeNode(value)
            return root
        else:
            q.append(node.right)
    return root

# Activity 2: Find Height / Depth of Tree
def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))

# Activity 3: Find Maximum value in Binary Tree
def find_max(root):
    if not root:
        return float('-inf')
    return max(root.val, find_max(root.left), find_max(root.right))

# Test
root = TreeNode(10)
insert_into_tree(root, 20)
insert_into_tree(root, 30)
insert_into_tree(root, 40)
print("Height of tree:", height(root))
print("Max value:", find_max(root))
