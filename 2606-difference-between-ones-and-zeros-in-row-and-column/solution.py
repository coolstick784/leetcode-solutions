class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows = {}
        cols = {}
        z_rows = {}
        z_cols = {}
        for r, row in enumerate(grid):
            for c, el in enumerate(row):
                rows[r] = rows.get(r, 0) + el
                cols[c] = cols.get(c, 0) + el
                z_rows[r] = z_rows.get(r, 0) + (el - 1) * -1
                z_cols[c] = z_cols.get(c, 0) + (el - 1) * -1
        res = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for r, row in enumerate(grid):
            for c, el in enumerate(row):
                res[r][c] = rows[r] + cols[c] - z_rows[r] - z_cols[c]
        return res
