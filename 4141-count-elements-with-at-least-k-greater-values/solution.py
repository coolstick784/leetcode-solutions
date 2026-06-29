class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        if k == 0:
            return len(nums)
        kth = len(nums) - k 
        res = kth
        while res-1 >= 0 and nums[res] == nums[res-1]:
            res -= 1

        return res
