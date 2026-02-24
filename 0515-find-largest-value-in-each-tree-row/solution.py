# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # We want a list of all the nodes in each row, as well as a list of all values in the next row
        # We can have a current row, next row, and next row values
        # At the end of the current row, add the maximum of the values to the resolution and set the current row to a copy of the next row
        # Also set the next row values to be empty
        # If our current row is empty, return blank
        if root is None:
            return []
        
        res = []
        cur_row = [root]
        next_row = []
        

        res.append(root.val)
        while cur_row != []:
            max_next_row_val = -2**31
            
            for node in cur_row:
                if node.left is not None:
                    next_row.append(node.left)
                    max_next_row_val = max(max_next_row_val, node.left.val)
                if node.right is not None:
                    next_row.append(node.right)
                    max_next_row_val = max(max_next_row_val, node.right.val)
            if next_row != []:
                res.append(max_next_row_val)
            cur_row = next_row.copy()
            next_row = []
        return res
