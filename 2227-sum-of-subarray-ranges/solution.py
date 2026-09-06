import heapq
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:

        res = 0
        for idx1, n1 in enumerate(nums):
            mn = float('inf')
            mx = -float('inf')

            for idx2, n2 in enumerate(nums[idx1:]):
                real_idx = idx1 + idx2
                mx = max(mx, n2)
                mn = min(mn, n2)

                
                res += mx - mn
        return res

