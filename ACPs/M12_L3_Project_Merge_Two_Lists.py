# Module 12 Lesson 3: After-Class Project
# Project Name: Sorted Linked List Combination Processing Pipeline

from M12_L1_Project_Singly_Linked_List import Node

def merge_sorted_linked_lists(list1_head, list2_head):
    dummy_root = Node(0)
    current_tail = dummy_root
    while list1_head and list2_head:
        if list1_head.data <= list2_head.data:
            current_tail.next = list1_head
            list1_head = list1_head.next
        else:
            current_tail.next = list2_head
            list2_head = list2_head.next
        current_tail = current_tail.next
    current_tail.next = list1_head if list1_head else list2_head
    return dummy_root.next

if __name__ == "__main__":
    l1 = Node(1); l1.next = Node(3)
    l2 = Node(2); l2.next = Node(4)
    merged = merge_sorted_linked_lists(l1, l2)
    print(f"Merged output tracking sequences head node value: {merged.data}")