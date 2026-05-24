class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        union_find = [[None for c in range(len(grid[0]))] for r in range(len(grid))]
        for r, row in enumerate(grid):
            for c, el in enumerate(row):
                if el == "1":
                    union_find[r][c] = (r, c)
        def trace(p):
            r, c = p
            if union_find[r][c] == (r, c):
                return (r, c)
            val = trace(union_find[r][c])
            union_find[r][c] = val
            return val
        def union(p1, p2):
            root1 = trace(p1)
            root2 = trace(p2)

            r2, c2 = root2
            union_find[r2][c2] = root1
            return 
        for r, row in enumerate(grid):
            for c, el in enumerate(row):
                if el == "1":
                    if r >0 and grid[r-1][c] == "1":
                        union((r-1, c), (r, c))
                    if c > 0 and grid[r][c-1] == "1":
                        union((r, c-1), (r, c))
        res = 0
        for r, row in enumerate(union_find):
            for c, el in enumerate(row): 
                if el == (r, c):
                    res += 1
        return res
