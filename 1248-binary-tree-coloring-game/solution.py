# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# either choose the parent or the child
# so if we choose the parent, it's total nodes - number of nodes starting from x
# if x is 1, parent is not an option
# if we choose a child, it's n -number of nodes starting from that child
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        
        num_nodes = {}
        @lru_cache(None)
        def getNodes(node):
            if node is None:
                return 0
            out = 1 + getNodes(node.left) + getNodes(node.right)
            num_nodes[node.val] = (out, node)
            return out


        getNodes(root)
        # if child
        max_nodes = 0 
        node_left_num = getNodes(num_nodes[x][1].left)
        node_right_num = getNodes(num_nodes[x][1].right)
        if node_right_num > n - node_right_num or node_left_num > n - node_left_num:
            return True
        # if parent
        if n - num_nodes.get(x, (0, 0))[0] > num_nodes.get(x, (0,0))[0]:
            return True
        return False
