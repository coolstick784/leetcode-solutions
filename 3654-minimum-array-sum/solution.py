# given an index, op1, and op2, what's the best we can do? move left to right
# nums = [2,8,3,19,3], k = 3, op1 = 1, op2 = 1
# 
class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        @lru_cache(None)
        def solve(idx, o1, o2):
            if idx == len(nums):
                return 0
            n = nums[idx]
            out = float('inf')
            # either op1, op2, op1 -> op2, or op2 -> op1
            if n >= k and o1 > 0 and o2 > 0:
                out = min(out, math.ceil((n-k)/2) + solve(idx+1, o1-1, o2-1))
            if math.ceil(n/2) >= k and o1 >0 and o2 > 0:
                out = min(out, math.ceil(n/2)-k + solve(idx+1, o1-1, o2-1))
            if n >= k and o2 > 0:
                out = min(out, n-k + solve(idx+1, o1, o2-1))
            if o1 > 0:
                out = min(out, math.ceil(n/2) + solve(idx+1, o1-1, o2))
            out = min(out, n + solve(idx+1, o1, o2))
            return out

        return solve(0, op1, op2)
