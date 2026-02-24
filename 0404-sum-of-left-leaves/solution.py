# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        res = 0
        while q:
            cur = q.popleft()
            

            if cur.left:
                if cur.left.left is None and cur.left.right is None:
                    res += cur.left.val
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

        return res
