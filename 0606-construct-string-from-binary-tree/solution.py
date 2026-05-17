# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            out = [str(node.val)]
            if node.left:
                out.append("(")
                out += dfs(node.left)
                out.append(")")
            if node.right and not node.left:
                out.append("(")
                out.append(")")
                out.append("(")
                out += dfs(node.right)
                out.append(")")
            elif node.right:
                out.append("(")
                out += dfs(node.right)
                out.append(")")
            return out
        return "".join(dfs(root))
