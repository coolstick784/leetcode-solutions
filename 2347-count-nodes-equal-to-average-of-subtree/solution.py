# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def solve(node): # return (number of subtrees, average, number of nodes)
            if not node:
                return (0, 0, 0, 0)
            left_sol, left_avg, lnum, lsum = solve(node.left)
            right_sol, right_avg, rnum, rsum = solve(node.right)
            res = left_sol + right_sol
            val = node.val
 
            avg = (node.val + lsum + rsum) / (lnum + rnum + 1)
            if int(avg) == node.val:
                res += 1
            print("val", node.val, "avg", avg)
            return (res, avg, lnum + rnum + 1, lsum + rsum + node.val)


        return solve(root)[0]


