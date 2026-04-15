# add edges
# we can create a componenet dict, which maps an edge to the component it's on
# the component # will be the minimum edge
# if we connect 2 by different components, subtract 1 from out conns list
# if components == k, return the edge we just pushed
class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        def find(x):
            if x == f[x]:
                return x
            f[x] = find(f[x])
            return f[x]

        def union(x, y):
            x = find(x)
            y = find(y)
            if x == y:
                return False
            f[x] = y
            return True

        if n <= k:
            return 0
        edges.sort(key = lambda e: e[2])
        count = n
        f = list(range(n))
        for u, v, w in edges:
            if union(u, v):
                count -= 1
            if count <= k:
                return w
