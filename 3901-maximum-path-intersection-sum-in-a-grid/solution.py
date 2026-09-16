# if at an edge, there have to be at least 2
class Solution:
    def maxScore(self, grid: list[list[int]]) -> int:
        rows = {}
        cols = {}
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                rows.setdefault(r, []).append(col)
                cols.setdefault(c, []).append(col)
        res = -float('inf')
        def solve(arr, edge=False):
            r = -float('inf')
            if not edge:
                cur = 0
                for idx, n in enumerate(arr):
                    cur += n
                    if idx > 0:
                        r = max(r, cur)
                    if idx < len(arr) - 2:
                        cur = max(cur, 0)
                return r
            cur = 0
            for idx, n in enumerate(arr):
                cur += n
                if idx > 0:
                    r = max(r, cur)
                
                cur = max(cur, n)
            return r
        for r in rows:
            cur = 0
            arr = rows[r]
            if r == 0 or r == len(grid) - 1:
                res = max(res, solve(arr, True))
            else:
                res = max(res, solve(arr))
        for c in cols:
            cur = 0
            arr = cols[c]
            if c == 0 or c == len(grid[0]) - 1:
                res = max(res, solve(arr, True))
            else:
                res = max(res, solve(arr))

        return res
