# 1. if a running sum if ever <0, remove everything up to the next index and restart the running sum
# if all numbers are <0, return the maximum of nums
# if a running sum is > 0, then the resolution is the max of (res, running_sum)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = 0
        run_sum = 0
        max_val = max(nums)
        if max_val < 0:
            return max_val
        for idx, n in enumerate(nums):
            run_sum += n
            if run_sum < 0:
                run_sum = 0
                
            else:
                res = max(res, run_sum)

        return res
