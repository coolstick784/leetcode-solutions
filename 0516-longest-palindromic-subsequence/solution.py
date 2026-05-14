# given a start and end index
#if start != end, we can either move the start over 1 or end over 1
# if start == end, we can also move in 2 and add 2 + longest palindrome, moving over 1 in both

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:


        @lru_cache(10_000)
        def solve(start, end):
            if start > end:
                return 0
            if start == end:
                return 1
            ch1 = s[start]
            ch2 = s[end]
            out = 0
            out = max(out, solve(start+1, end))
            out = max(out, solve(start, end-1))
            if ch1 == ch2:
                out = max(out, 2+solve(start+1, end-1))
            return out
        
        return solve(0, len(s) - 1)
        
