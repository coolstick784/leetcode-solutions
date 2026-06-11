class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        
        conns = {}
        for start, end in edges:
            conns.setdefault(start, set()).add(end)
            conns.setdefault(end, set()).add(start)
        def explore(n, parent=None):
            res = 0
            for end in conns.get(n, set()):
                if end == parent:
                    continue

                res = max(res, 1 + explore(end, n))
            return res

        maxDepth = explore(1)

            




        return 2**(maxDepth-1) % (10**9+7)
