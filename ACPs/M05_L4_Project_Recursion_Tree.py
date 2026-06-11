# Module 5 Lesson 4: After-Class Project
# Project Name: Recursive Directory Tree Traversal File System Simulation Engine

class VirtualFileSystemNode:
    def __init__(self, name, is_directory=False):
        self.name = name
        self.is_dir = is_directory
        self.children = []

def print_virtual_tree_recursive(node, depth_indentation_level=0):
    indent = "  " * depth_indentation_level
    marker = "[DIR] " if node.is_dir else "[FILE] "
    print(f"{indent}{marker}{node.name}")
    
    for child in node.children:
        print_virtual_tree_recursive(child, depth_indentation_level + 1)

if __name__ == "__main__":
    root = VirtualFileSystemNode("Root_Server", is_directory=True)
    bin_dir = VirtualFileSystemNode("bin", is_directory=True)
    bin_dir.children.append(VirtualFileSystemNode("python3.exe"))
    root.children.append(bin_dir)
    root.children.append(VirtualFileSystemNode("config.json"))
    
    print("--- Simulating Recursive FS Tree Nodes Generation ---")
    print_virtual_tree_recursive(root)