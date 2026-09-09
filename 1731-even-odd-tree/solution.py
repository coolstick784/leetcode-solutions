# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        mn_mx = {}
        def solve(node, level):
            if not node:
                return True
            if level % 2 == node.val % 2:
                return False
            val = node.val
            if level % 2 == 1:
                if val >= mn_mx.get(level, float('inf')):
                    return False
                
            else: 
                if val <= mn_mx.get(level, -float('inf')):
                    return False
            mn_mx[level] = val
            #print(mn_mx)
            return solve(node.left, level + 1) and solve(node.right, level +1)

                
        return solve(root, 0)
