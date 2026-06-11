# Module 13 Lesson 4: After-Class Project
# Project Name: Invert Binary Tree Structural Mirror Image Flipping Engine

def execute_tree_inversion(root_node):
    if not root_node: return None
    root_node.left, root_node.right = execute_tree_inversion(root_node.right), execute_tree_inversion(root_node.left)
    return root_node

if __name__ == "__main__":
    from M13_L1_Project_Binary_Tree_Traversals import TreeNode
    root = TreeNode(1); root.left = TreeNode(2); root.right = TreeNode(3)
    execute_tree_inversion(root)
    print(f"Inverted mirror state logic mapping verification left child target value: {root.left.val}")