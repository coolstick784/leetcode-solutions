# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# we can either say this is already monitored, pass it to its children, or put a camera there
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        @lru_cache(None)
        def solve(node, self_need, parent_need):
            if node is None:
                if parent_need:
                    return float('inf')
                return 0
            out = []
            # there is no scenario where your parent needs it but you don't
            if self_need and not parent_need:
                out.append(1 + solve(node.left, False, False) + solve(node.right, False, False)) # add camera
                out.append(solve(node.left, True, True) + solve(node.right, True, False)) # make the left node cover it
                out.append(solve(node.right, True, True) + solve(node.left, True, False)) # make the right cover it
            elif self_need and parent_need:
                out.append(1 + solve(node.left, False, False) + solve(node.right, False, False)) #add camera
            else: # dont need and parent doesnt need
                out.append(1 + solve(node.left, False, False) + solve(node.right, False, False)) # add camera to cover children
                out.append(solve(node.left, True, False) + solve(node.right, True, False)) # make children cover themselves
            return min(out)
            

            

        return solve(root, True, False)
