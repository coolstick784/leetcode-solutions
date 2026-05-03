class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        NEG = -10**18

        k = min(k, m + n - 1)

        dp = [[NEG] * (k + 1) for _ in range(n)]

        start_cost = 1 if grid[0][0] != 0 else 0
        if start_cost > k:
            return -1

        dp[0][start_cost] = grid[0][0]

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue

                cost_here = 1 if grid[r][c] != 0 else 0
                score_here = grid[r][c]

                cur = [NEG] * (k + 1)

                for used in range(cost_here, k + 1):
                    prev_used = used - cost_here

                    from_top = dp[c][prev_used]

                    from_left = NEG
                    if c > 0:
                        from_left = dp[c - 1][prev_used]

                    best_prev = max(from_top, from_left)

                    if best_prev != NEG:
                        cur[used] = best_prev + score_here

                dp[c] = cur

        best = max(dp[n - 1])
        return best if best != NEG else -1
