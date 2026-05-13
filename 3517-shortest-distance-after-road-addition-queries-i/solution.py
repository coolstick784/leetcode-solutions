class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        res = []
        edges = {}

        for start, end in queries:
            edges.setdefault(start, []).append(end)

            @lru_cache(None)
            def solve(idx):
                if idx == n - 1:
                    return 0

                out = 1 + solve(idx + 1)

                for edge in edges.get(idx, []):
                    out = min(out, 1 + solve(edge))

                return out

            res.append(solve(0))

        return res
