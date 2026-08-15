class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @lru_cache(None)
        def solve(r, c, moves):
            print("r", r, "c", c, "moves", moves)
            if r < 0 or r >= m or c < 0 or c >= n:
                return 1
            if moves == 0:
                return 0
            return solve(r-1, c, moves-1) + solve(r+1, c, moves-1) + solve(r, c+1, moves-1) + solve(r, c-1, moves-1)
        return solve(startRow, startColumn, maxMove) % (10**9+7)
