# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def solve(cur_l):
            if cur_l == []:
                return None
            cur_val = max(cur_l)
            cur_idx = cur_l.index(cur_val)
            return TreeNode(val=cur_val, left=solve(cur_l[:cur_idx]), right=solve(cur_l[cur_idx+1:]))
        return solve(nums)
