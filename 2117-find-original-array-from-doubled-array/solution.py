class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        ctr = Counter(changed)
        res = []
        for c in changed:
            if ctr.get(c, 0) == 0:
                continue
            elif c == 0 and ctr.get(0, 0) >= 2:
                ctr[0] -= 2
                res.append(0)
            elif c!= 0 and ctr.get(c*2, 0) > 0:
                ctr[c] -= 1
                ctr[c*2] -= 1

                res.append(c)
            else:
                return []
        return res
