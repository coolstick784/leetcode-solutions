
# [1, 1, 2, 4] 1 and 2, 1 and 4
# [1, 2, 3, 4] 1 and 3, 2 and 4
# [1, 2, 4, 4] [1 and 4, 2 and 4]

class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        mid = len(nums) // 2
        left = 0
        right = mid
        res = 0
        while left < mid and right < len(nums):
            if nums[left] * 2 <= nums[right]:
                res += 2
                left += 1
                right += 1
            else:
                right += 1
        return res
