# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, mn, mx):
            if node is None:
                return True
            if node.val <= mn or node.val >= mx:
                return False
            if not valid(node.left, mn, min(node.val, mx)):
                return False
            if not valid(node.right, max(node.val, mn), mx):
                return False
            return True

        return valid(root, -float('inf'), float('inf'))
