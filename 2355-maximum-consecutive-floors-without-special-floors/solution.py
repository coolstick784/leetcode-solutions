class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        res = 0
        b = bottom
        for s in special:
            res = max(res, s - b)
            b = s + 1
        res = max(res, top - b + 1)
        return res
