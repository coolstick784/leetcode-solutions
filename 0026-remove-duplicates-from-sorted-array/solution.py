class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        while idx < len(nums):

            if idx >= 1 and nums[idx] in nums[:idx]:
                nums.remove(nums[idx])
            else:
                idx += 1

        return len(nums)
