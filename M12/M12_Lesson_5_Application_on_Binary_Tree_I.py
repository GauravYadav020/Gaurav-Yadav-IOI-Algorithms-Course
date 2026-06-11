"""
M12 Lesson 5 – Application on Binary Tree I

Applications: Finding diameter, checking balanced tree, etc.
"""

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

# Activity 1: Check if Binary Tree is Balanced
def is_balanced(root):
    def height(node):
        if not node:
            return 0
        left_h = height(node.left)
        right_h = height(node.right)
        if abs(left_h - right_h) > 1:
            return -1  # unbalanced
        return 1 + max(left_h, right_h)
    return height(root) != -1

# Activity 2: Find Diameter of Binary Tree
def diameter_of_tree(root):
    def depth(node):
        if not node:
            return 0
        left = depth(node.left)
        right = depth(node.right)
        diameter[0] = max(diameter[0], left + right)
        return 1 + max(left, right)
    diameter = [0]
    depth(root)
    return diameter[0]

# Activity 3: Sum of all nodes
def sum_of_nodes(root):
    if not root:
        return 0
    return root.val + sum_of_nodes(root.left) + sum_of_nodes(root.right)

# Test
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print("Is Balanced?", is_balanced(root))
print("Diameter:", diameter_of_tree(root))
print("Sum of all nodes:", sum_of_nodes(root))
