import bisect
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        mx = -float('inf')
        new = []
        for idx, (p, b) in enumerate(items):
            if b > mx:
                new.append((p, b))
                mx = b
            else:
                continue
        prices = [0] + [i[0] for i in new]
        beauties = [0] + [i[1] for i in new]
        res = []
        for p in queries:
            b = beauties[bisect.bisect(prices, p) - 1]
            res.append(b)
        return res

