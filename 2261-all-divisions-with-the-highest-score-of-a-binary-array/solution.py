class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        left = 0
        l0 = 0
        l1 = 0
        mx = -float('inf')
        res = []
        for idx, n in enumerate(nums):
            if n == 1:
                l1 += 1
        for idx, n in enumerate(nums):
            cur = l0 + l1
            if cur > mx:
                res = [idx]
                mx = cur
            elif cur == mx:
                res.append(idx)
            if n == 0:
                l0 += 1
            else:
                l1 -= 1
        cur = l0 + l1
        if cur > mx:
            res = [len(nums)]
            mx = cur
        elif cur == mx:
            res.append(len(nums))
        return res

