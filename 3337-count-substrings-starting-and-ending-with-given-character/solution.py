class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        ctr = 0
        res = 0
        for ch in s:
            if ch == c:
                res += ctr + 1
                ctr += 1
        return res
