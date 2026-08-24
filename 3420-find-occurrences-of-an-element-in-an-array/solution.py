class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        idxs = {}
        for idx, n in enumerate(nums):
            idxs.setdefault(n, []).append(idx)
        res = []
        for q in queries:
            if len(idxs.get(x, [])) < q:
                res.append(-1)
            else:
                res.append(idxs[x][q-1])
        return res

