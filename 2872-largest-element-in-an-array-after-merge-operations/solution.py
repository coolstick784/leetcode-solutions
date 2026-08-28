from collections import deque
class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        cur = nums[-1]
        res = nums[-1]
        
        for idx in range(len(nums)-2, -1, -1):
            n = nums[idx]
            if n > cur:
                cur = n
            else:
                cur += n
            res = max(res, cur)
        return res
            
            
            
            
