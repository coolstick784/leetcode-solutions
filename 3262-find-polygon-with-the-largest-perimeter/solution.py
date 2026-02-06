class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        res = -1
        cur_sum = 0
        for idx, n in enumerate(nums):
            if idx >= 2 and cur_sum > n:
                cur_sum += n
                res = cur_sum
            else:
                cur_sum += n
        return res
