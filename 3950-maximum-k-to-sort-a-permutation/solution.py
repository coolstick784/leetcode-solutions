class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        s = sorted(nums)
        res = float('inf')
        if s == nums:
            return 0

        idxs = {}
        for idx, n in enumerate(nums):
            idxs[n] = idx

        for idx, n in enumerate(nums):
            should = s[idx]
            if n == should:
                continue
            if res != float('inf'):
                res = min(res, (n & should) & res)
            else:
                res = n & should
            idxs[n] = idxs[should]
            idxs[should] = idx
        return res
