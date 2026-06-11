# Module 13 Lesson 2: After-Class Project
# Project Name: Tree Height Structural Metric Depth Profiler Engine

def calculate_tree_max_depth(root_node):
    if not root_node: return 0
    return 1 + max(calculate_tree_max_depth(root_node.left), calculate_tree_max_depth(root_node.right))

if __name__ == "__main__":
    from M13_L1_Project_Binary_Tree_Traversals import TreeNode
    root = TreeNode(1); root.left = TreeNode(2); root.left.left = TreeNode(3)
    print(f"Calculated maximum distance tree structure leaf paths metrics: {calculate_tree_max_depth(root)}")