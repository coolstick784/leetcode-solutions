# if n-1 nodes have parents, and no node has two parents, and each node is accounted for we're good
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        def possible(idx):
            n = len(edges)
            descendants = {}
            starts = {}
            nodes = set()
            for i, (start, end) in enumerate(edges):
                if i == idx:
                    continue
                descendants.setdefault(end, set()).add(start)
                if len(descendants[end]) > 1:
                    return False
                if end in descendants.get(start, set()):
                    return False
                nodes.add(start)
                nodes.add(end)
            roots = 0
           
            for i in range(1, n+1):
                if i not in descendants:
                    roots += 1
            return len(nodes) == n and roots == 1
        
        for idx in range(len(edges)-1, -1, -1):
            if possible(idx):
                return edges[idx]
