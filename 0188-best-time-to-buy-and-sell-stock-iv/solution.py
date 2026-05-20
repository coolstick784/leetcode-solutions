class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        @lru_cache(None)
        def solve(idx, buy, sell, hold):
            if idx == len(prices):
                return 0
            out = 0
            if hold and sell:
                out = max(out, prices[idx] + solve(idx+1,buy, sell-1, False))
            out = max(out, solve(idx+1, buy, sell, hold))
            if not hold and buy:
                out = max(out, -prices[idx] + solve(idx+1, buy-1, sell, True))
            return out

        return solve(0, k,k, False)
            
