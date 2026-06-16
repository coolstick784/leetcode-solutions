# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        sols = set()
        dups = set()
        res = []


        def s(node):
            if node is None:
                return "None"
            left = s(node.left)
            right = s(node.right)
            return f"{node.val}, {left}, {right}"
        def explore(node):
            
            if node is None:
                return
            
            inSols = False
            inDups = False
            cur = s(node)
            if cur in sols:
                inSols = True

            if cur in dups:
                inDups = True
            if inSols and not inDups:
                res.append(node)
                dups.add(cur)

            
            elif not inDups and not inSols:
                sols.add(cur)
            
            explore(node.left)
            explore(node.right)
        explore(root)

        return res
