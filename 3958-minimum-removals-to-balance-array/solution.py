class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        res = float('inf')
        for r in range(len(nums)):
            while nums[l] < nums[r] / k:
                l += 1
            res = min(res, len(nums) - (r-l+1))
        return res
