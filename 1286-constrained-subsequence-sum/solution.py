
# if it's a positive number, obviously take it
# 

from collections import deque
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        
        res = max(nums)
        dp = deque() # highest to lowest val, lowest to highest idx
        for idx, n in enumerate(nums):

            while dp and idx - k > dp[0][1]:
                dp.popleft()
            cur = 0
            if dp:
                cur = max(dp[0][0], 0)
            cur += n
            while dp and cur >= dp[-1][0]:
                dp.pop()
            if cur >= 0:
                dp.append((cur, idx))
            res = max(res, cur)



        return res

        
