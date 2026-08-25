MOD = 10**9+7
class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        dp = {}
        def solve(x, y, cur):
            if (x, y, cur) in dp:
                return dp[(x, y, cur)]
            if cur > 32:
                return 0
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                return 0
            if x == len(grid) - 1 and y == len(grid[0]) - 1 and cur == grid[x][y]:
                return 1
            val = grid[x][y]
            res = (solve(x+1, y, cur ^ val) + solve(x, y+1, cur ^ val)) % MOD
            dp[(x, y, cur)] = res
            return res


        return solve(0, 0, k)
