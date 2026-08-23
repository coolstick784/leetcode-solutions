class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        ctr = Counter(arr)
        diff = 0
        while len(res) < k:
            while len(res) < k and ctr.get(x-diff, 0) > 0:
                res.append(x-diff)
                ctr[x-diff] -= 1
            while len(res) < k and ctr.get(x+diff, 0) > 0:
                res.append(x+diff)
                ctr[x+diff] -= 1
            diff += 1 
        return sorted(res)
