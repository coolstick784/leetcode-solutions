# we either cut the longest in 2 or there are 2 next to each other

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        past = 0
        res = 1
        prev = -float('inf')
        cur = 0
        for idx, n in enumerate(nums):
            if n > prev:
                cur += 1
                
            else:

                past = cur
                cur = 1
            res = max(res, cur // 2)
            
            res = max(res, min(cur, past))
            prev = n
        
        return res
            

