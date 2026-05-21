class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def solve(idx, hold):
            if idx >= len(prices):
                return 0
            out = 0
            if hold:
                out = max(out, prices[idx] + solve(idx+2, False))
            out = max(out, solve(idx+1, hold))
            if not hold:
                out = max(out, solve(idx+1, True) - prices[idx])
            return out


        return solve(0, False)
