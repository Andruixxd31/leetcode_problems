# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        unique = set()
        while head:
            unique.add(head)
            head = head.next
            if head in unique:
                return True
        return False
            
