class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        ctr = {}
        for r, row in enumerate(grid):
            for c, el in enumerate(row):
                ctr.setdefault(c, {})
                ctr[c][el] = ctr[c].get(el, 0) + 1
        @lru_cache(None)
        def solve(col, prev):

            res = float('inf')
            if col >= len(grid[0]):
                return 0
            for idx in range(12):
                if idx == prev:
                    continue
                cost = rows - ctr[col].get(idx, 0)
                
                res = min(res, cost + solve(col+1, idx))
                
           
            return res


        return solve(0, (0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
