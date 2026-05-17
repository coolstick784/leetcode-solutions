# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



# [3], [9, 20], [15, 7]
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = deque([[] for _ in range(3000)])

        def explore(node, level):
            if node is None:
                return
            levels[level].append(node.val)
            explore(node.left, level+1)
            explore(node.right, level+1)

        explore(root, 0)
        levels.reverse()
        print("levels", levels)
        while levels and levels[0] == []:
            levels.popleft()
        
        return list(levels)
        
