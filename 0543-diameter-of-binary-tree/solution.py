# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# how many nodes max can we go to the left and down, vs how many nodes are to the right and down?
# use dfs, it's 1 + max dist (left) + 1 + max_dist (right)
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def explore(node):
            if node is None:
                return 0
            
            out = 0
            explore_left = explore(node.left)
            explore_right = explore(node.right)
            max_dist = 1 + max(explore_left, explore_right)
            self.res = max(self.res, explore_left+explore_right)
            return max_dist
        explore(root)
        return self.res

