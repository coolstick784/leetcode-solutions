# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # Initialize a global variable to store the result
        global ans
        ans = 0

        # Helper function to perform depth-first search
        def dfs(root, start):
            global ans

            # Base case: if the current node is None, return 0 and False
            if root is None:
                return 0, False

            # Recursive calls for the left and right subtrees
            left, found_in_left = dfs(root.left, start)
            right, found_in_right = dfs(root.right, start)

            # If the current node's value is equal to the target 'start'
            if root.val == start:
                # Update the global result with the maximum of current and children's depths
                ans = max(ans, max(left, right))
                return 1, True

            # If 'start' is found in the left subtree
            if found_in_left:
                # Update the global result with the sum of left and right depths
                ans = max(ans, right + left)
                return left + 1, True

            # If 'start' is found in the right subtree
            elif found_in_right:
                # Update the global result with the sum of left and right depths
                ans = max(ans, right + left)
                return right + 1, True

            # If 'start' is not found in either subtree
            else:
                # Return the maximum depth of the left and right subtrees + 1, and False
                return max(left, right) + 1, False

        # Call the dfs function with the root and start values
        dfs(root, start)
        # Return the final result
        return ans
