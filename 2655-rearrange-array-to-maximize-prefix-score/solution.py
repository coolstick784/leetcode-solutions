class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort()
        nums.reverse()
        res = 0
        cur = 0
        for n in nums:
            cur += n
            if cur > 0:
                res += 1
        return res
