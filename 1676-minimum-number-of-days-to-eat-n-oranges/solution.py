# we either go for the next n/2 or next n/3
class Solution:
    def minDays(self, n: int) -> int:

        @lru_cache(None)
        def solve(cur):
            if cur == 1:
                return 1
            if cur == 0:
                return 0
            out = float('inf')
            out = min(out, cur%2+1 + solve(cur//2))
            out = min(out, cur%3+1 + solve(cur//3))
            return out

        return solve(n)
        
