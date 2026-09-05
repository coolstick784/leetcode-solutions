class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        i1 = set()
        i2 = set()
        def search(r, c):
            if (r, c) in i1 or r >= len(grid) or c >= len(grid[0]) or r <0 or c < 0 or grid[r][c] == 0:
                return
            i1.add((r, c))
            search(r+1, c)
            search(r-1, c)
            search(r, c+1)
            search(r, c-1)
        for r, row in enumerate(grid):
            for c, col in enumerate(grid):
                el = grid[r][c]
                if el == 0:
                    continue
                to_add = False
                if i1 == set():
                    search(r, c)
                if (r, c) not in i1:
                    i2.add((r, c))
        res = float('inf')
        print(i1)
        print(i2)
        for r1, c1 in i1:
            for r2, c2 in i2:
                res = min(res, abs(r1-r2) + abs(c1-c2)-1)
        return res
