"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


# pass in the node and the one that should be to the right
# do dfs so we don't overwrite anything at the top
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q = deque([(root, 0)])
        prev = (None, 0)
        
        while q:
            
            node, level = q.popleft()
            if node is None:
                continue
            if prev[1] == level:
                node.next = prev[0]
            else:
                node.next = None
            q.append((node.right, level+1))
            q.append((node.left, level+1))
            prev = (node, level)


        return root
