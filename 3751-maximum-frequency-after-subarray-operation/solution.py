class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        mn = min(nums)
        mx = max(nums)
        base = nums.count(k)
        max_diff = 0
        for n in range(mn, mx+1):
            ct_k = 0
            ct_n = 0
            for idx, num in enumerate(nums):
                if num == k:
                    ct_k += 1
                if num == n:
                    ct_n += 1
                if ct_k >= ct_n:
                    ct_k = 0
                    ct_n = 0
                max_diff = max(max_diff, ct_n - ct_k)
        return base + max_diff
