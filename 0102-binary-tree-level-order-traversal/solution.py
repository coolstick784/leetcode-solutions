from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        keys = deque([root])   # like your "keys", but queue of nodes
        res = []
        cur_level = 0

        while keys:
            level_size = len(keys)
            cur_res = []

            # process exactly this level
            for _ in range(level_size):
                cur_node = keys.popleft()
                cur_res.append(cur_node.val)

                if cur_node.left is not None:
                    keys.append(cur_node.left)
                if cur_node.right is not None:
                    keys.append(cur_node.right)

            res.append(cur_res)
            cur_level += 1

        return res

