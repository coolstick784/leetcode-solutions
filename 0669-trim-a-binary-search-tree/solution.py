# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Keep looking left (can also go right from left, but check left first) for the first one < the current node but > the low, then set that as prev_node.left
# and add it to the q
# Do the same thing looking to the right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:

        new_root = root
        while new_root.val < low or new_root.val > high:
            if new_root.val < low:
                new_root = new_root.right
            else:
                new_root = new_root.left
            if new_root is None:
                return None
       
        q = deque([new_root])
        while q:
            cur = q.popleft()

            new_node = cur.left
            while new_node is not None and new_node.val < low:
                new_node = new_node.right

            cur.left = new_node
            if new_node is not None:
                q.append(new_node)

            new_node = cur.right
            while new_node is not None and new_node.val > high:
                new_node = new_node.left
            cur.right = new_node
            if new_node is not None:
                q.append(new_node)

        
        return new_root
        
