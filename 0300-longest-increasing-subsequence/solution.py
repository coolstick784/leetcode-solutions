class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        best = 1
        @lru_cache(None)
        def solve(start_idx):
            cur = 1
            for idx in range(start_idx+1, len(nums)):
                if nums[idx] > nums[start_idx]:
                    cur = max(cur, 1 + solve(idx))
            return cur
        for start_idx in range(len(nums)):
            best = max(best, solve(start_idx))

        return best
