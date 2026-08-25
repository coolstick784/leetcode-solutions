# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        levels = {}
        def explore(node, level):
            if not node:
                return 
            levels[level] = levels.get(level, 0) + 1
            explore(node.left, level + 1)
            explore(node.right, level + 1)

        explore(root, 0)
        mx = max(levels.keys())
        
        n = levels[mx]
        res = (None, -1) #node, level
        def solve(node, level):
            if not node:
                return 0
            nonlocal res
            nonlocal n
            nonlocal mx
            num = 0
            if level == mx:
                num = 1
            num += solve(node.left, level + 1)
            num += solve(node.right, level + 1)
            if num == n and level > res[1]:
                res = (node, level)
            return num


        solve(root, 0)
        return res[0]
        
