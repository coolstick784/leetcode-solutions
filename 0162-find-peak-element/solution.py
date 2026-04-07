class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # a peak is when (nums[i] > nums[i-1]) or i == 0 and (nums[i] > nums[i+1]) or i == len(nums) - 1
        # start from the middle
        # move to the middle of the higher side
        left = 0
        right = len(nums) - 1
        while left <= right:
            med = (left + right) // 2
            val = nums[med]
            if (med == 0 or nums[med-1] < val) and (med == len(nums) - 1 or nums[med+1] < val):
                return med
            if (med == 0 or nums[med-1] < val): # something greater to the right
                left = med + 1
            else: # something greater to the left
                right = med - 1
