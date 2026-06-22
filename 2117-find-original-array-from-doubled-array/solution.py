from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        ctr = Counter(changed)
        res = []
        for idx in range(len(changed) -1, -1, -1):
            n = changed[idx]

            if ctr[n] > 0:
                ctr[n] -= 1
                if n % 2 == 1 or ctr.get(n//2, 0) <= 0:
                    return []
                res.append(n//2)

                ctr[n//2] -= 1
        return res
