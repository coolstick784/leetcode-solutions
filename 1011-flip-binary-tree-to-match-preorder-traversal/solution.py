# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        idxs = {}
        for idx, n in enumerate(voyage):
            idxs[n] = idx
        
        res = []
        def dfs(node):
            if not node:
                return 

            if (node.left and node.right and idxs[node.left.val] > idxs[node.right.val]):
                node.left, node.right = node.right, node.left
                res.append(node.val)
            dfs(node.left)
            dfs(node.right) 


        

        dfs(root)
        new = []
        def create(node):
            if not node:
                return 
            new.append(node.val)
            create(node.left)
            create(node.right)


        create(root)
        return res if -1 not in res and new == voyage else [-1]
