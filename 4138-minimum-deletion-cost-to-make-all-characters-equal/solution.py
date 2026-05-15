class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        totalCost = 0
        cost_chars = {}
        for idx, ch in enumerate(s):
            totalCost += cost[idx]
            cost_chars[ch] = cost_chars.get(ch, 0) + cost[idx]
        res = float('inf')
        if len(set(s)) == 1:
            return 0
        for ch in cost_chars:
            
            res = min(res, totalCost-cost_chars[ch])
        return res
