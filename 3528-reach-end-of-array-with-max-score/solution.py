class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        cur = 0
        mx = 0
        for idx, n in enumerate(nums):
            cur += mx
            mx = max(mx, n)
        return cur
            
