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
        if root is None:
            return None
        new_left = self.invertTree(root.right)
        new_right = self.invertTree(root.left)
        root.left = new_left
        root.right = new_right
        return root
