# Module 14 Lesson 2: After-Class Project
# Project Name: High Precision BST Range Boundary Constraints Validator

def validate_bst_intervals(node, low_limit=float('-inf'), high_limit=float('inf')):
    if not node: return True
    if not (low_limit < node.val < high_limit): return False
    return validate_bst_intervals(node.left, low_limit, node.val) and validate_bst_intervals(node.right, node.val, high_limit)

if __name__ == "__main__":
    from M13_L1_Project_Binary_Tree_Traversals import TreeNode
    root = TreeNode(10); root.left = TreeNode(5); root.right = TreeNode(2) # Invalid configuration tracking rules bounds
    print(f"Does input network tree align with legal BST properties? {validate_bst_intervals(root)}")