# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        i_idxs = {n:idx for idx, n in enumerate(inorder)}

        preorder = deque(preorder)
        def solve(left, right):
            if left > right or not preorder:
                return None
            node = TreeNode(preorder.popleft())
            mid = i_idxs[node.val]
            node.left = solve(left, mid-1)
            node.right = solve(mid+1, right)
            return node



        return solve(0, len(preorder) - 1)
