# left and a right
# first, len = right - left + 1
# res = max(res, len)
# if right +1 > right and we're not at the end, move the right 1
# otherwise, move the left to the right


# [1, 3, 5, 4, 7] while right < 4 
# 


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        left = 0
        right = 0
        res = 1
        while left < len(nums) and right < len(nums):

            while right < (len(nums) -1 ) and nums[right+1] > nums[right]:
                right += 1
            l = right - left + 1
            res = max(res, l)
            left = right + 1
            right = left
            

        return res
