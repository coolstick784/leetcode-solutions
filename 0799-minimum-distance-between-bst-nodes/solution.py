# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        vals = []
        res = float('inf')
        def explore(node):
            nonlocal res
            if node is None:
                return
            for v in vals:
                res = min(res, abs(node.val-v))
            vals.append(node.val)
            explore(node.left)
            explore(node.right)
        explore(root)
        return res
