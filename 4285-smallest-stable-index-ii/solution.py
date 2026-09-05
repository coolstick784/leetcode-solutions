class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        small = [None for _ in nums]
        cur = float('inf')
        for idx in range(len(nums)-1, -1, -1):
            cur = min(cur, nums[idx])
            small[idx] = cur
        cur = -float('inf')
        for idx, n in enumerate(nums):
            cur = max(cur, n)
            if cur - small[idx] <= k:
                return idx

        return -1
