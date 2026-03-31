class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node, mask):
            if not node:
                return

            # flip the bit for this value
            mask ^= (1 << node.val)

            # leaf node
            if not node.left and not node.right:
                if mask & (mask - 1) == 0:
                    self.res += 1
                return

            dfs(node.left, mask)
            dfs(node.right, mask)

        dfs(root, 0)
        return self.res
