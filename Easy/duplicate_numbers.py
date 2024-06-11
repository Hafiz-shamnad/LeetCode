'''
Remove Duplicates from Sorted List

Given the head of a sorted linked list, delete all duplicates such that each element 
appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        
        return head

# Helper functions for testing
def list_to_linkedlist(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linkedlist_to_list(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst

# Example usage
sol = Solution()

# Example 1
head = list_to_linkedlist([1, 1, 2])
new_head = sol.deleteDuplicates(head)
print(linkedlist_to_list(new_head))  # Output: [1, 2]

# Example 2
head = list_to_linkedlist([1, 1, 2, 3, 3])
new_head = sol.deleteDuplicates(head)
print(linkedlist_to_list(new_head))  # Output: [1, 2, 3]
