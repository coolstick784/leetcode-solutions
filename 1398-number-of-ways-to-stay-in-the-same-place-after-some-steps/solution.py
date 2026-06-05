class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        arrLen = min(arrLen, steps//2+1)
        @lru_cache(None)
        def solve(start, s):
            out = 0

            if start > s or start >= arrLen or start < 0:
                return 0
            if s == start:
                return 1
            out += solve(start, s-1)

            out += solve(start-1, s-1)

            out += solve(start+1, s-1)
    
            return out % (10**9+7)
        return solve(0, steps) 
        
