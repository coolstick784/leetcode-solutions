class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cur = 2
        res = 2
        for idx, n in enumerate(nums):
            if idx < 2:
                continue
            if n == nums[idx-2] + nums[idx-1]:
                cur += 1
            else:
                cur = 2
            res = max(res, cur)
        return res
