# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        vals = {}
        def dfs(node, level):
            if node is None:
                return
            vals.setdefault(level, []).append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        dfs(root, 0)
        for i in vals:
            vals[i].reverse()
            vals[i] = deque(vals[i])
        def solve(node, level):
            if node is None:
                return None
            node.left = solve(node.left, level + 1)
            node.right = solve(node.right, level + 1)

            if level % 2 == 0:
                return node
            node.val = vals[level].popleft()
            return node
            
 
        return solve(root, 0)
