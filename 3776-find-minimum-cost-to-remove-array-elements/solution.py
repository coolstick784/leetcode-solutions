class Solution:
    def minCost(self, nums: List[int]) -> int:
        @lru_cache(10**4)
        def solve(s1, idx):
            if idx >= len(nums):
                return s1
            if idx == len(nums) - 1:
                return max(s1, nums[idx])
            out = float('inf')
            out = min(out, max(s1, nums[idx]) + solve(nums[idx+1], idx+2))
            out = min(out, max(nums[idx+1], nums[idx]) + solve(s1, idx+2))
            out = min(out, max(s1, nums[idx+1]) + solve(nums[idx], idx+2))



            return out
        

        return solve(nums[0], 1)
