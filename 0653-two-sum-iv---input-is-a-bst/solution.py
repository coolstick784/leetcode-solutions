# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # have a set of all numbers so far
        # goal is k - current
        # if our goal is in the set, return True
        # otherwise, at the end, return false
        # have a stack of all nodes we want to look at
        
        
        nums = set()
        stack = [root]
        while stack:
            cur = stack.pop()
            if not cur:
                continue
            goal = k - cur.val
            if goal in nums:
                return True
            nums.add(cur.val)
            stack.append(cur.left)
            stack.append(cur.right)
                
        
        return False
