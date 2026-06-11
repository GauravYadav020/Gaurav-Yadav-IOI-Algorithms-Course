"""
M12 Lesson 4 – Tree Traversals

1. Preorder (Root-Left-Right)
2. Inorder (Left-Root-Right)
3. Postorder (Left-Right-Root)
4. Level Order
"""

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

# Activity 1: Preorder Traversal
def preorder(root, result):
    if root:
        result.append(root.val)
        preorder(root.left, result)
        preorder(root.right, result)

# Activity 2: Inorder Traversal
def inorder(root, result):
    if root:
        inorder(root.left, result)
        result.append(root.val)
        inorder(root.right, result)

# Activity 3: Level Order Traversal
from collections import deque

def level_order(root):
    if not root:
        return []
    result = []
    q = deque([root])
    while q:
        node = q.popleft()
        result.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return result

# Test
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

res = []
preorder(root, res)
print("Preorder:", res)

res = []
inorder(root, res)
print("Inorder:", res)

print("Level Order:", level_order(root))
