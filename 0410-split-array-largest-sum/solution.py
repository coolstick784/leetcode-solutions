


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        sums = []
        cur = 0
        for n in nums:
            cur += n
            sums.append(cur)
        @lru_cache(None)
        def solve(idx, n):
            if idx == len(nums) and n == 1:
                return 0
            elif idx == len(nums):
                return float('inf')
            if n == 1:
                return nums[idx] + solve(idx+1, 1)
            if n < 1:
                return float('inf')
            
            cur = 0
            out = float('inf')
            for i in range(idx, len(nums)):
                cur += nums[i]
                out = min(out, max(cur, solve(i+1, n-1)))
            print(idx, n, out)
            return out


        return solve(0, k)
