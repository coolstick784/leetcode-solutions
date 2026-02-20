from typing import List

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        R, C = len(coins), len(coins[0])
        NEG_INF = -10**18

        # dp[r][c][t] = max sum to reach (r,c) using t neutralizations (t=0..2)
        dp = [[[NEG_INF] * 3 for _ in range(C)] for _ in range(R)]

        # init at (0,0)
        v = coins[0][0]
        if v >= 0:
            dp[0][0][0] = v
        else:
            dp[0][0][0] = v          # don't neutralize
            dp[0][0][1] = 0          # neutralize it

        for r in range(R):
            for c in range(C):
                if r == 0 and c == 0:
                    continue

                v = coins[r][c]

                # look from top and left
                candidates = []
                if r > 0: candidates.append((r - 1, c))
                if c > 0: candidates.append((r, c - 1))

                for pr, pc in candidates:
                    for t in range(3):
                        prev = dp[pr][pc][t]
                        if prev == NEG_INF:
                            continue

                        if v >= 0:
                            dp[r][c][t] = max(dp[r][c][t], prev + v)
                        else:
                            # take the negative
                            dp[r][c][t] = max(dp[r][c][t], prev + v)
                            # neutralize (if we still can)
                            if t < 2:
                                dp[r][c][t + 1] = max(dp[r][c][t + 1], prev)

        return max(dp[R - 1][C - 1])

