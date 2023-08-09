# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        node = dummy
        while dummy:
            if dummy.next and dummy.next.val == val:
                tmp = dummy.next
                dummy.next = tmp.next
                tmp.next = None
            else:
                dummy = dummy.next
        return node.next
