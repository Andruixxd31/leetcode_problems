# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        if self.traverse(root) == False:
            return None

        return root

    def traverse(self, node):
        if node is None:
            return

        if self.traverse(node.left) == False:
            node.left = None
        if self.traverse(node.right) == False:
            node.right = None

        if node.val == 0 and node.left is None and node.right is None:
            return False
