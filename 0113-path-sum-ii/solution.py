# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # Do a breadth first search
        # There should be a global res arr
        # We want to pass in the current sum, current list, and the goal
        # If the current sum + value is equal to the goal, add the current list + [value] to the resolution
        # Keep going unless both left and right are None
        self.res = []
        def bfs(node, cur_sum = 0, cur_list = []):
            if node is None:
                return
            if cur_sum + node.val == targetSum and node.left is None and node.right is None:
                self.res.append(cur_list + [node.val])
            bfs(node.left, cur_sum + node.val, cur_list + [node.val])
            bfs(node.right, cur_sum + node.val, cur_list + [node.val])
        
        bfs(root)
        return self.res
