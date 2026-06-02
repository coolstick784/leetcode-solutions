# 1. if a running sum if ever <0, remove everything up to the next index and restart the running sum
# if all numbers are <0, return the maximum of nums
# if a running sum is > 0, then the resolution is the max of (res, running_sum)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = 0
        cur = 0
        mx = max(nums)
        if mx <= 0:
            return mx
        for n in nums:
            cur += n
            if cur <= 0:
                cur = 0
            res = max(res, cur)
        return res
