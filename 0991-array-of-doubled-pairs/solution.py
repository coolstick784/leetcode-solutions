from collections import Counter

# 1 = 2 * 0
# 3 = 2 * 1
# 5 = 2 * 4
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        pos = [n for n in arr if n >= 0]
        neg = [-n for n in arr if n < 0]
        def solve(cur):
            if len(cur) % 2 == 1:
                return False
            cur.sort()
            ctr = Counter(cur)
            for idx, n in enumerate(cur):
                if ctr[n] > 0:
                    ctr[n] -= 1
                else:
                    continue
                if ctr.get(n*2, 0) > 0:
                    ctr[n*2] -= 1
                else:
                    return False
            return True
        return solve(pos) and solve(neg)
