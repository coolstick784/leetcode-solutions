"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        new_nodes = {}
        explored = set()
        def dfs(og_node, new_node):
            new_nodes[og_node.val] = new_node
            new_node.neighbors = []
            if og_node.neighbors:
                
                for n in og_node.neighbors:
                    if n.val in new_nodes:
                        new_node.neighbors.append(new_nodes[n.val])
                    else:
                        new_node.neighbors.append(dfs(n, Node(n.val)))
            return new_node
                        
        if not node:

            return None
        if not node.neighbors:
            return Node(node.val)
        return dfs(node, Node(node.val))
