class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        map_dict = {}
        for idx, edge in enumerate(edges):
            start, end = edge
            map_dict.setdefault(start, []).append(end)
            map_dict.setdefault(end, []).append(start)
        explored = set()

        def findMax(n):
            out = [0]
            explored.add(n)
            for end in map_dict[n]:
                if end not in explored:
                    out.append(1+findMax(end))
            return max(out)


        max_depth = findMax(1)

        def solve(n, isEven):
            return 2**(n-1)
        return solve(max_depth, False) % (10**9+7)
