class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mx = max(nums)
        mn = min(nums)
        for idx, n in enumerate(nums):

            if n == mx:
                mx_idx = idx
            if n == mn:
                mn_idx = idx
        
        mx_idx, mn_idx = max(mx_idx, mn_idx), min(mx_idx, mn_idx)
        return min(mx_idx+1, len(nums) - mn_idx, mn_idx+1 + len(nums) - mx_idx)
