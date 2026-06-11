# LESSON NAME: M13 Lesson 4 – Deletion on a Binary Search Tree

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Corporate offboarding directory. Delete single-child/leaf profiles.
# ==========================================
class EmpNode:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name
        self.left = self.right = None

class EnterpriseDirectory:
    def __init__(self): self.root = None
    def add(self, emp_id, name):
        if not self.root: self.root = EmpNode(emp_id, name); return
        curr = self.root
        while True:
            if emp_id < curr.emp_id:
                if not curr.left: curr.left = EmpNode(emp_id, name); break
                curr = curr.left
            else:
                if not curr.right: curr.right = EmpNode(emp_id, name); break
                curr = curr.right
    def remove_leaf(self, root, target_id):
        if not root: return None
        if target_id < root.emp_id: root.left = self.remove_leaf(root.left, target_id)
        elif target_id > root.emp_id: root.right = self.remove_leaf(root.right, target_id)
        else:
            if not root.left and not root.right: return None
            if not root.left: return root.right
            if not root.right: return root.left
        return root

print("--- Activity 1: Offboarding Profile Removal ---")
directory = EnterpriseDirectory()
directory.add(50, "Manager")
directory.root = directory.remove_leaf(directory.root, 50)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Two-child deletion in active Task Dispatcher Pipeline using Inorder Successor.
# ==========================================
class TaskNode:
    def __init__(self, weight, job_name):
        self.weight = weight
        self.job_name = job_name
        self.left = self.right = None

class TaskPipelineBST:
    def __init__(self): self.root = None
    def push(self, weight, job_name):
        def _push(node):
            if not node: return TaskNode(weight, job_name)
            if weight < node.weight: node.left = _push(node.left)
            else: node.right = _push(node.right)
            return node
        self.root = _push(self.root)
    def _get_min(self, node):
        while node.left: node = node.left
        return node
    def delete_task(self, root, weight):
        if not root: return root
        if weight < root.weight: root.left = self.delete_task(root.left, weight)
        elif weight > root.weight: root.right = self.delete_task(root.right, weight)
        else:
            if not root.left: return root.right
            if not root.right: return root.left
            temp = self._get_min(root.right)
            root.weight = temp.weight
            root.right = self.delete_task(root.right, temp.weight)
        return root

print("\n--- Activity 2: Two-Child Pipeline Deletion ---")
pipeline = TaskPipelineBST()
pipeline.push(60, "Job A")
pipeline.root = pipeline.delete_task(pipeline.root, 60)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Memory tracking allocation backend simulation with dynamic defrag calculations.
# ==========================================
class MemoryBlock:
    def __init__(self, addr, size):
        self.addr = addr
        self.size = size
        self.left = self.right = None

class MemoryControllerBST:
    def __init__(self): self.root = None
    def allocate(self, addr, size):
        if not self.root: self.root = MemoryBlock(addr, size)
    def collect_total_size(self, node):
        if not node: return 0
        return node.size + self.collect_total_size(node.left) + self.collect_total_size(node.right)

print("\n--- Activity 3: Memory Allocator System ---")
ctrl = MemoryControllerBST()
ctrl.allocate(0x00A1, 1024)
print(f"Total Allocated Memory Space: {ctrl.collect_total_size(ctrl.root)} KB")