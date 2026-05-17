class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 0
        while left < len(nums):
            right = max(left, right)
            if nums[left] == 0:
                while right < len(nums) and nums[right] == 0:
                    right += 1
                if right < len(nums):
                    nums[left], nums[right] = nums[right], nums[left]


            left += 1

