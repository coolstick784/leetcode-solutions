# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# pass in if its parent is even, as well as if it is even, and then the child node
# if the paren't parent is even, res ++ 1
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def solve(gp, parent, node):
            if not node:
                return 
            if gp:
                self.res += node.val
            is_even = False
            if node.val %2 == 0:
                is_even = True
            solve(parent, is_even, node.left)
            solve(parent, is_even, node.right)
            

        solve(False, False, root)
        return self.res
