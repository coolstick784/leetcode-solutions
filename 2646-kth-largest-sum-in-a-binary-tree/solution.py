# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sums = {}
        def explore(level, node):
            if not node:
                return
            sums[level] = sums.get(level, 0) + node.val
            explore(level+1, node.left)
            explore(level+1, node.right)

        explore(0, root)
        vals = sorted(list(sums.values()))
        if len(vals) < k:
            return -1
        return vals[-k]
