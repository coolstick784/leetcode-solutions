class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def best(idx, have):
            if idx == len(prices):
                return 0
            out = 0
            if have:
                out = max(out, prices[idx] + best(idx+1, False))
            else:
                out = max(out, -prices[idx] + best(idx+1, True))
                
            out = max(out, best(idx+1, have))
            return out


        return best(0, False)
