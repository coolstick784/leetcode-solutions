class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diag = {}
        rows = {}
        for r, row in enumerate(nums):
            for c, el in enumerate(row):
                rows.setdefault(c, []).append(r)
        for c in rows:
            for r in rows[c]:
   
                el = nums[r][c]
                d = c + r
                diag.setdefault(d, []).append(el)
        res = []
        keys = sorted(list(diag.keys()))
        for k in keys:
            res.extend(diag[k])
        return res
