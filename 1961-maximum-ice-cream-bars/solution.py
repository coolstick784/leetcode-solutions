from collections import Counter
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        mx = max(costs)
        res = 0
        ctr = Counter(costs)
        for n in range(1, mx+1):
            ct = ctr.get(n, 0) 
            cost = n * ct
            if cost < coins:
                coins -= cost
                res += ct
            else:
                res += coins // n
                coins -= (n * coins // n)
            
        return res
