# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast, slow = head, dummy

        for i in range(n):
            fast = fast.next
        
        while fast:
            fast = fast.next
            slow = slow.next
        
        tmp = slow.next
        slow.next = tmp.next
        tmp.next = None

        return dummy.next
