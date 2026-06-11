# Module 13 Lesson 5: After-Class Project
# Project Name: Tree Lowest Common Ancestor Node Location Resolver

def locate_lca(root, p_node, q_node):
    if not root or root == p_node or root == q_node: return root
    left_scan = locate_lca(root.left, p_node, q_node)
    right_scan = locate_lca(root.right, p_node, q_node)
    if left_scan and right_scan: return root
    return left_scan if left_scan else right_scan

if __name__ == "__main__":
    from M13_L1_Project_Binary_Tree_Traversals import TreeNode
    root = TreeNode(3); root.left = TreeNode(5); root.right = TreeNode(1)
    print(f"LCA Convergence execution mapping point tracking resolved: {locate_lca(root, root.left, root.right).val}")