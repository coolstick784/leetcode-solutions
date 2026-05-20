class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.pre_idx = 0
        def build(inord):
            if not inord:
                return None

            node = TreeNode(preorder[self.pre_idx])
            self.pre_idx += 1
            idx = inord.index(node.val)

            node.left = build(inord[:idx])
            node.right = build(inord[idx+1:])
            return node
        return build(inorder)
