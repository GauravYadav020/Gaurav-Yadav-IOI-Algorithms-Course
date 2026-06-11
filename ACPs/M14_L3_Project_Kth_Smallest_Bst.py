# Module 14 Lesson 3: After-Class Project
# Project Name: BST Inorder Inversion Pipeline Kth Smallest Element Extractor

def extract_kth_smallest_bst(root_node, target_k):
    elements_array = []
    def inorder_traverse(node):
        if node and len(elements_array) < target_k:
            inorder_traverse(node.left)
            elements_array.append(node.val)
            inorder_traverse(node.right)
    inorder_traverse(root_node)
    return elements_array[target_k - 1]

if __name__ == "__main__":
    from M13_L1_Project_Binary_Tree_Traversals import TreeNode
    root = TreeNode(20); root.left = TreeNode(10); root.right = TreeNode(30)
    print(f"Extracted Kth sequence node matching metric priority: {extract_kth_smallest_bst(root, 2)}")