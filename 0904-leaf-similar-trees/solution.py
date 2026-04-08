# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# we'll want to define a function that gets the sequence, then compare the two
# we'll want to return the sequence of the left of the node + the sequence of the right so they're in order
# if both right and left are none, return [<val>]
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getSequence(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            return getSequence(node.left) + getSequence(node.right)
            
        
        return getSequence(root1) == getSequence(root2)
