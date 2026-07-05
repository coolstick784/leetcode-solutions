class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for idx, n in enumerate(nums):
            if idx == 0:
                continue
            if n <= nums[idx-1]:
                res += (nums[idx-1]+1-n)
                nums[idx] = nums[idx-1] + 1
        return res
