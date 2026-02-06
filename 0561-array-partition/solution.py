class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for idx in range(len(nums)-2, -2, -2):
            cur = nums[idx]
            res += cur
        return res
        
