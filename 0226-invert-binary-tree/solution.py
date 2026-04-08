# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# have a stack of the nodes we want to go to
# add the left and the right to the stack and switch them
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur is None:
                continue
            cur.left, cur.right = cur.right, cur.left
            stack.append(cur.left)
            stack.append(cur.right)
        return root
