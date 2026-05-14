class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        def solve(idx, given):
            if idx == len(s):
                return 0
            res = -float('inf')
            for idx2 in range(idx, len(s)):
                if s[idx:idx2+1] not in given:
                    res = max(res, 1 + solve(idx2+1, given + [s[idx:idx2+1]]))
            return res

        return solve(0, [])
