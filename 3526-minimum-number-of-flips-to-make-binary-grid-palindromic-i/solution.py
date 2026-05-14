# for a specific row or col, if start != end, add 1, then move in
# do this for all rows, then all cols, then get the min from each

class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:

        def minRC(cells):
            start = 0
            end = len(cells) - 1
            out = 0
            while start < end:
                if cells[start] != cells[end]:
                    out += 1
                start += 1
                end -= 1
            return out
        
        rows = [r for r in grid]
        cols = [[] for _ in grid[0]]
        for r, row in enumerate(grid):
            for c, el in enumerate(row):
                cols[c].append(el)
        min_rows = 0
        min_cols = 0
        for row in rows:
            min_rows += minRC(row)
        for col in cols:
            min_cols += minRC(col)

        return min(min_rows, min_cols)
        
