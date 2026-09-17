# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        def solve(node):
            if not node:
                return (0, -float('inf'))
            n_left, mx_left = solve(node.left)

            n_right, mx_right = solve(node.right)
            if mx_left == -float('inf') and mx_right == -float('inf'):
                comp = node.val
            else:
                comp = max(mx_left, mx_right)
            return (n_left + n_right + (node.val >= comp), max(node.val, mx_left, mx_right))

        return solve(root)[0]
