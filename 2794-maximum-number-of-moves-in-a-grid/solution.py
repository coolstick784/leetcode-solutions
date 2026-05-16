class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        @lru_cache(None)
        def solve(row, col):
            
            out = 0
            if row > 0 and col < len(grid[0]) -1 and grid[row-1][col+1] > grid[row][col]:
                out = max(out, 1+solve(row-1, col+1))
            if col < len(grid[0]) -1 and grid[row][col+1] > grid[row][col]:
                out = max(out, 1+solve(row, col+1))
            if row < len(grid) - 1 and col < len(grid[0]) -1 and grid[row+1][col+1] > grid[row][col]:
                out = max(out, 1+solve(row+1, col+1))
            return out
        
        res = 0
        for r in range(len(grid)):
            res = max(res, solve(r, 0))
        return res
