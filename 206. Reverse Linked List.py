"""
206. Reverse Linked List
Easy

Given the head of a singly linked list, reverse the list, and return the reversed list.

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            # Save the next node before overwriting the pointer
            next_node = curr.next 
            
            # Reverse the pointer to point backwards
            curr.next = prev      
            
            # Move the pointers one step forward for the next iteration
            prev = curr
            curr = next_node
            
        # At the end, 'curr' is None, and 'prev' is the new head of the reversed list
        return prev

# ---------------------------------------------------------
# Helper functions and Test block to run locally
# ---------------------------------------------------------
def create_linked_list(arr: list[int]) -> Optional[ListNode]:
    """Helper function to create a linked list from a Python list."""
    dummy = ListNode(0)
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linked_list_to_list(head: Optional[ListNode]) -> list[int]:
    """Helper function to convert a linked list back to a Python list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    input_arr1 = [1, 2, 3, 4, 5]
    head1 = create_linked_list(input_arr1)
    reversed_head1 = solution.reverseList(head1)
    print(f"Input: head = {input_arr1}")
    print(f"Output: {linked_list_to_list(reversed_head1)}\n")
    
    # Test case 2
    input_arr2 = [1, 2]
    head2 = create_linked_list(input_arr2)
    reversed_head2 = solution.reverseList(head2)
    print(f"Input: head = {input_arr2}")
    print(f"Output: {linked_list_to_list(reversed_head2)}\n")
    
    # Test case 3
    input_arr3 = []
    head3 = create_linked_list(input_arr3)
    reversed_head3 = solution.reverseList(head3)
    print(f"Input: head = {input_arr3}")
    print(f"Output: {linked_list_to_list(reversed_head3)}")