class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        @lru_cache(None)
        def solve(idx, a_idx):

            if a_idx == len(a) and idx <= len(b):
                return 0
            if a_idx >= len(a) or idx >= len(b):
                return -float('inf')

            res = solve(idx+1, a_idx)
            res = max(res, a[a_idx] * b[idx] + solve(idx+1, a_idx+1))
            return res

        return solve(0, 0)
