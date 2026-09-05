class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        goal = sum(nums) / 2
        if sum(nums) % 2 == 1:
            return False
        @lru_cache(None)
        def solve(idx, cur):
            if cur == 0:
                return True
            if cur < 0:
                return False
            if idx >= len(nums):
                return False
            return solve(idx+1, cur - nums[idx]) or solve(idx+1, cur)
        return solve(0, goal)
