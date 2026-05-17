class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        for idx in range(len(nums) -2, -1, -1):
            if nums[idx] >= nums[idx+1]:
                return idx + 1
        return 0
