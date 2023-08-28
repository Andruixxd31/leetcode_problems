# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        stA, stB = [], []
        while headA:
            stA.append(headA)
            headA = headA.next

        while headB:
            stB.append(headB)
            headB = headB.next
        
        res = ListNode()
        while stA and stB:
            nodeA = stA.pop()
            nodeB = stB.pop()
            if nodeA == nodeB:
                res = nodeA
            else: 
                break
        if res.val != 0: return res
        else: return None
