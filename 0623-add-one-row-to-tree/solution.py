# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            head = TreeNode(val=val)
            head.left = root
            return head


        def solve(node, cur, val, depth):
            if not node:
                return None
            node.left = solve(node.left, cur+1, val, depth)
            node.right = solve(node.right, cur+1, val, depth)
            if cur == depth - 1:
                prev_left = node.left
                prev_right = node.right
                new_left = TreeNode(val=val)
                new_left.left = prev_left
                new_right = TreeNode(val=val)
                new_right.right = prev_right
                node.left = new_left
                node.right = new_right

            return node

        return solve(root, 1, val, depth)
