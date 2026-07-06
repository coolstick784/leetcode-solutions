from functools import lru_cache
class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        @lru_cache(None)
        def solve(idx, selected, right):
            if selected == len(slices) // 3:
                return 0
            if idx > right:
                return -float('inf')
            out = -float('inf')
            out = max(out, slices[idx] + solve(idx+2, selected+1, right))
            out = max(out, solve(idx+1, selected, right))
            return out

        
        return max(solve(0, 0, len(slices)-2), solve(1, 0, len(slices)-1))
