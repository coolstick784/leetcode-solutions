class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(None)
        def solve(idx1, idx2):
            if idx1 >= len(text1) or idx2 >= len(text2):
                return 0
            res = solve(idx1+1, idx2)
            res = max(res, solve(idx1, idx2+1))
            if text1[idx1] == text2[idx2]:
                res = max(res, 1 + solve(idx1+1, idx2+1))
            return res
        return solve(0, 0)
