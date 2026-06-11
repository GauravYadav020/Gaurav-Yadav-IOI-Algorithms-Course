# Module 14 Lesson 1: After-Class Project
# Project Name: BST Sorted Space Structural Element Insertion Matrix

from M13_L1_Project_Binary_Tree_Traversals import TreeNode

class BinarySearchTreeModel:
    def inject_key(self, root_node, target_key):
        if not root_node: return TreeNode(target_key)
        if target_key < root_node.val:
            root_node.left = self.inject_key(root_node.left, target_key)
        else:
            root_node.right = self.inject_key(root_node.right, target_key)
        return root_node

if __name__ == "__main__":
    bst = BinarySearchTreeModel()
    root = TreeNode(50)
    bst.inject_key(root, 30); bst.inject_key(root, 70)
    print(f"BST structural logic bounds validated right node track value: {root.right.val}")