class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def solve(n):
            if n < 0:
                return float('inf')
            if n == 0:
                return 0
            out = float('inf')
            for c in coins:
                out = min(out, 1 + solve(n-c))
            return out
        if solve(amount) == float('inf'):
            return -1
        return solve(amount)
