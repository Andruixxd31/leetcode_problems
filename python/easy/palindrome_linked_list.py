# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        node = head
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        
        while node:
            if node.val == stack[-1]:
                stack.pop()
                node = node.next
            else:
                return False
        return True
