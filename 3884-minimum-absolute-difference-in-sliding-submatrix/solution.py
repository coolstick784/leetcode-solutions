class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        res = []
        @lru_cache(None)
        def solve(r, c):
            if r > len(grid) - k:
                return None
            if c > len(grid[0]) - k:
                return None

            vals = []
            for r1 in range(r, r+k):
                for c1 in range(c, c+k):
                    el = grid[r1][c1]
                    vals.append(el)
            res = float('inf')

            vals = list(set(vals))
            if len(vals) == 1:
                return 0
            vals.sort()
            for idx, v in enumerate(vals[:-1]):
                res = min(res, vals[idx+1]-v)
            print("r", r, "c", c, "res", res)
            return res

        for r, row in enumerate(grid):
            cur = []
            for c, el in enumerate(row):
                if solve(r, c) is not None:
                    cur.append(solve(r, c))
            if cur:
                res.append(cur)
        return res
                
