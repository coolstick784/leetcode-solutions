# to move from one start to the next, we add the sum of all numbers, and then subtract 2*the new start
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        s = sum(nums)
        n = len(nums)


        total = 0
        for idx, num in enumerate(nums):
            total += num * idx
        res = total

        for start in range(n-1, 0, -1):
            total += s
            total -= (n * nums[start])
 
            res = max(res, total)
        return res



