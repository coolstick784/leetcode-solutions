class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        max_val = max(costs)
        counts = [0 for _ in range(max_val+1)]
        for c in costs:
            counts[c] += 1
        cur = 0
        res = 0
        for idx, _ in enumerate(counts):
            while counts[idx] > 0 and cur + idx <= coins:

                cur += idx
                res += 1
                counts[idx] -= 1
        return res
        
