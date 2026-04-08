# at each price, we want to set our maximum to our max of (maximum, price - (minimum up to and including this point))
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        cur_min = inf
        for idx, p in enumerate(prices):
            if p < cur_min:
                cur_min = p
            res = max(p - cur_min, res)
        return res
        
