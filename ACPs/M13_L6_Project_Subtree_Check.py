# Module 13 Lesson 6: After-Class Project
# Project Name: Hierarchical Structural Subtree Identity Matching Matrix

def match_exact_trees(t1, t2):
    if not t1 and not t2: return True
    if not t1 or not t2: return False
    return t1.val == t2.val and match_exact_trees(t1.left, t2.left) and match_exact_trees(t1.right, t2.right)

def verify_is_subtree(root_tree, candidate_subtree):
    if not root_tree: return False
    if match_exact_trees(root_tree, candidate_subtree): return True
    return verify_is_subtree(root_tree.left, candidate_subtree) or verify_is_subtree(root_tree.right, candidate_subtree)

if __name__ == "__main__":
    from M13_L1_Project_Binary_Tree_Traversals import TreeNode
    r = TreeNode(1); r.left = TreeNode(2)
    sub = TreeNode(2)
    print(f"Is target subtree nested within validation framework structure matrix? {verify_is_subtree(r, sub)}")