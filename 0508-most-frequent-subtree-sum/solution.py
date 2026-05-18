# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# ctr with each sum
# get the max count
# for each value, if it has the max ct, add it to res
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.ctr = {}

        def addSum(node):
            if node is None:
                return 0
            cur = node.val
            cur += addSum(node.left)
            cur += addSum(node.right)
            self.ctr[cur] = self.ctr.get(cur,0)+1
            return cur 
        addSum(root)
        max_ct = max(self.ctr.values())
        res = []
        for val, ct in self.ctr.items():
            if ct == max_ct:
                res.append(val)
        return res
