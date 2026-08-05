# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = {}
        def explore(node, level):
            if not node:
                return
            levels[level] = node.val
            explore(node.left, level+1)
            explore(node.right, level+1)

        explore(root, 0)

        keys = sorted(levels.keys())
        return [levels[key] for key in keys]
