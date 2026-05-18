class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        best = [[-float('inf') for _ in grid[0]] for _ in grid]
        res = -float('inf')

        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):

                # best value reachable from below
                if r + 1 < rows:
                    best[r][c] = max(best[r][c], grid[r + 1][c], best[r + 1][c])

                # best value reachable from right
                if c + 1 < cols:
                    best[r][c] = max(best[r][c], grid[r][c + 1], best[r][c + 1])

                # use that best future value to compute score
                res = max(res, best[r][c] - grid[r][c])

        return res
