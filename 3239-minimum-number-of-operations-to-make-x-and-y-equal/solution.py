from functools import lru_cache

class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        @lru_cache(None)
        def solve(n):
            if n <= y:
                return y - n

            ans = n - y

            q, r = divmod(n, 11)
            ans = min(ans, r + 1 + solve(q))          # subtract r, then divide by 11
            ans = min(ans, (11 - r) + 1 + solve(q+1)) # add (11-r), then divide by 11

            q, r = divmod(n, 5)
            ans = min(ans, r + 1 + solve(q))          # subtract r, then divide by 5
            ans = min(ans, (5 - r) + 1 + solve(q+1)) # add (5-r), then divide by 5

            return ans

        return solve(x)
