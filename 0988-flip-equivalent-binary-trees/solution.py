# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def canEqual(node1, node2):
            if node1 is None and node2 is None:
                return True
            
            if node1 is None or node2 is None or node1.val != node2.val:
                
                return False
            if node1.left and node2.left and node2.right and node1.right and node1.left.val == node2.right.val:
                return canEqual(node1.left, node2.right) and canEqual(node1.right, node2.left)
            if node1.left and not node2.left:
                return canEqual(node1.left, node2.right) and canEqual(node1.right, node2.left)
            if node1.right and not node2.right:
                return canEqual(node1.left, node2.right) and canEqual(node1.right, node2.left)
            return canEqual(node1.left, node2.left) and canEqual(node1.right, node2.right) 

        return canEqual(root1, root2)
