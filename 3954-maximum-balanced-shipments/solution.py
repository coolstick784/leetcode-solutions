class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        mx = -float('inf')
        res = 0
        for idx, w in enumerate(weight):
            if w < mx:
                mx = -float('inf')
                res += 1
            else:
                mx = max(mx, w)
        return res
