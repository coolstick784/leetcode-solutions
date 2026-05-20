

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None

        node = TreeNode(postorder.pop())
        idx = inorder.index(node.val)


        node.right = self.buildTree(inorder[idx+1:], postorder)
        node.left = self.buildTree(inorder[:idx], postorder)
        return node
