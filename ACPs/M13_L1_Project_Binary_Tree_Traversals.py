# Module 13 Lesson 1: After-Class Project
# Project Name: Binary Tree Multi-Pass Traversal Deep Processing System

class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = self.right = None

class TreeTraversalEngine:
    def compute_inorder(self, root_node, out_list):
        if root_node:
            self.compute_inorder(root_node.left, out_list)
            out_list.append(root_node.val)
            self.compute_inorder(root_node.right, out_list)

if __name__ == "__main__":
    root = TreeNode(10); root.left = TreeNode(5); root.right = TreeNode(15)
    engine = TreeTraversalEngine()
    res = []
    engine.compute_inorder(root, res)
    print(f"Tree structure dynamic inorder validation array: {res}")