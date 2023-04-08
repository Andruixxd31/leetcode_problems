# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        
        def getDepth(root):
            nonlocal res
            if not root: return 0
            l = getDepth(root.left)
            r = getDepth(root.right)
            if abs(l - r) > 1: res = False
            return(max(l,r) + 1)
        getDepth(root)
        return res
