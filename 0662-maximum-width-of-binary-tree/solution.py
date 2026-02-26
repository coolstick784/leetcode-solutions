# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # We need to calculate the overall index of each node that exists, as well as save each node to the levels
        # 0.left = 1, 0.right = 2, 1.left = 3, 1.right = 4, 2.left = 5, 2.right = 6
        # start is 2^(n-1) -1, end = 2^n - 2
        # diff from curr to the curr start * 2 + next level start + 1 if right
        cur_level = deque([(root, 0)])
        level = 0
        max_dist = 0
        while cur_level:
 
            max_dist = max(max_dist, cur_level[-1][1] - cur_level[0][1] + 1)
            cur_start = 2**level-1
            next_start = 2**(level+1)-1
            for _ in range(len(cur_level)):
                cur_node, cur_idx = cur_level.popleft()
                
                calc_next = next_start + (cur_idx - cur_start) * 2 
                if cur_node.left is not None:
                    cur_level.append((cur_node.left, calc_next))
                if cur_node.right is not None:
                    cur_level.append((cur_node.right, calc_next+1))

                
            level += 1
        
        
        return max_dist
