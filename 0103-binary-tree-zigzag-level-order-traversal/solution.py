# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# [3,9,20,null,null,15,7]
# [3] new q = [9, 20]
# [9, 20] new q = [7, 15, none, none]
# 
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        res = []
        level = 1
        while q:
            new_q = deque()
            cur = []
            while q:
                if level % 2 == 1:
                    node = q.pop()
                    if node:
                        cur.append(node.val)
                        new_q.append(node.left)
                        new_q.append(node.right)
                else:
                    node = q.pop()
                    if node:
                        cur.append(node.val)
                        new_q.append(node.right)
                        new_q.append(node.left)

            
            if cur:
                res.append(cur)
            q = new_q.copy()
            level += 1
        return res
