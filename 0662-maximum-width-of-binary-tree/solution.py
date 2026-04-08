# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# go through each level, left to right
# we want to know what each index "should be"
# for example, the left -> left -> left should be 0

# 0 -> [0, 1]
# 1 -> [2, 3]
# 3 -> [6, 7]
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        cur_level = [(0, root)]
        res = 1
        next_level = []
        while cur_level:
            res = max(res, cur_level[-1][0] - cur_level[0][0] + 1)
            for idx, node in cur_level:
                if node.left is not None:
                    next_level.append((idx*2, node.left))
                if node.right is not None:
                    next_level.append((idx*2+1, node.right))
   
            
            cur_level = next_level.copy()
            next_level = []
        return res
        


        
