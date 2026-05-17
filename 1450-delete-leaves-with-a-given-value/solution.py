# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# if left, explore the left
# if right, explore the right
# if leftand right are None, and the value is the target, delete it
# return the node to its parent


# 1 -> 2 -> 2 -> node.left = None 
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def explore(node):
            if node.left:
                node.left = explore(node.left)
            if node.right:
                node.right = explore(node.right)
            if not node.left and not node.right and node.val == target:
                node = None
            return node

        return explore(root)
