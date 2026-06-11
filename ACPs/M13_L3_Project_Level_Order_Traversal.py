# Module 13 Lesson 3: After-Class Project
# Project Name: BFS Queue Breadth First Tree Level Matrix Mapper

from collections import deque

def compute_level_order_matrix(root_node):
    if not root_node: return []
    out, queue = [], deque([root_node])
    while queue:
        level_size = len(queue)
        current_level_elements = []
        for _ in range(level_size):
            curr = queue.popleft()
            current_level_elements.append(curr.val)
            if curr.left: queue.append(curr.left)
            if curr.right: queue.append(curr.right)
        out.append(current_level_elements)
    return out

if __name__ == "__main__":
    from M13_L1_Project_Binary_Tree_Traversals import TreeNode
    root = TreeNode(1); root.left = TreeNode(2); root.right = TreeNode(3)
    print(f"BFS Matrix Tree layout layers configuration maps: {compute_level_order_matrix(root)}")