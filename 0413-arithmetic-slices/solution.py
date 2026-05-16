# everything at the previous index minus 1 (max of 0, so we can't do -1), BUT if the next difference is different than the previous difference, we have to re=explore


# [1, 2, 3, 5, 7, 9] 1
# 


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        res = 0
        left = 0
        right = 0
        while left < len(nums):
            if (right - left + 1) < 3 and (left+1) < len(nums):
                right = left
                diff = nums[left+1] - nums[left]
                while right < len(nums)-1 and nums[right+1] - nums[right] == diff:
                    right += 1
            

            if (right - left + 1) >= 3:
                res += (right - left + 1 - 2)
            
            left += 1
        return res
