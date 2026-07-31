squares = set()
for n in range(1, 10**2+1):
    squares.add(n*n)
s_sq = set(squares)
squares = list(set(squares))
squares.sort()


from collections import Counter
# two perfect squares will be perfect squares
# two of the same number will be perfect squares
# 
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        nums = [0] + nums
        best = [n for n in nums]
        res = 0
        for idx, n in enumerate(nums):
            
            if idx == 0:
                continue
            cur = 0
            for s in squares:
                cur_idx = idx * s
              
                if cur_idx >= len(nums):
                    break
                cur += nums[cur_idx]
                res = max(res, cur)
      
        return res

