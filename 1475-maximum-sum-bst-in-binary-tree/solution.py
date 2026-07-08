# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node): # return sum, max, min
            if not node:
                return (0, -float('inf'), float('inf'))
            nonlocal res
            s_left, mx_left, mn_left = dfs(node.left)
            s_right, mx_right, mn_right = dfs(node.right)
            cur = node.val + s_left + s_right
            if cur != -float('inf') and node.val > mx_left and node.val < mn_right:
                res = max(res, cur)
            else:
                cur = -float('inf')
            
            if cur == -float('inf'):
                return (-float('inf'), float('inf'), -float('inf'))
            return (cur, max(node.val, mx_left, mx_right), min(node.val, mn_left, mn_right))


        dfs(root)
        return res


        
