class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        run = 0
        res = 0
        for idx, n in enumerate(nums):
            if n == 0:
                run += 1
            else:
                run = 0
            res += run
        return res
