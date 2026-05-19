# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return []
            cur = [node.val]
            out = []
            for li in dfs(node.left):
                out.append(cur + li)

            for li in dfs(node.right):
                out.append(cur + li)
            if not out:
                return [cur]
            return out
            


        lis = dfs(root)
       
        res = 0
        for li in lis:
            i = "".join([str(ch) for ch in li])
            res += int(i)
        return res
