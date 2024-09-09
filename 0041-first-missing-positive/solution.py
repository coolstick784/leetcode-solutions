class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        min_num = 1
        nums.sort()
        for num in nums:
            if num == min_num:
                min_num += 1
        return min_num
        
