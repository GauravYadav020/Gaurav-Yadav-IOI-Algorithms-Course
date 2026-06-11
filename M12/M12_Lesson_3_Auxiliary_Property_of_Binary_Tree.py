"""
M12 Lesson 3 – Auxiliary Property of Binary Tree

Properties like: Full Binary Tree, Complete Binary Tree, Perfect Binary Tree,
Balanced Binary Tree, etc.
"""

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

# Activity 1: Check if Binary Tree is Full
def is_full_binary_tree(root):
    if not root:
        return True
    if (root.left is None and root.right is None):
        return True
    if (root.left is not None and root.right is not None):
        return is_full_binary_tree(root.left) and is_full_binary_tree(root.right)
    return False

# Activity 2: Check if Complete Binary Tree (using level order)
from collections import deque

def is_complete_tree(root):
    if not root:
        return True
    q = deque([root])
    flag = False
    while q:
        node = q.popleft()
        if node.left:
            if flag:
                return False
            q.append(node.left)
        else:
            flag = True
        if node.right:
            if flag:
                return False
            q.append(node.right)
        else:
            flag = True
    return True

# Activity 3: Count Leaf Nodes
def count_leaves(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)

# Test
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print("Is Full Binary Tree?", is_full_binary_tree(root))
print("Is Complete Binary Tree?", is_complete_tree(root))
print("Number of leaves:", count_leaves(root))
