class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        idx = len(nums) // 2
        if nums[idx] == k:
            return 0
        cost = 0
        if nums[idx] > k:
            while idx >= 0 and nums[idx] > k:
                cost += nums[idx] - k
                idx -= 1
        else:
            while idx < len(nums) and nums[idx] < k:
                cost += k - nums[idx]
                idx += 1
        return cost
