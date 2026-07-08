# option 4 needs to be > (2*option 1 )

class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 20000:
            return 1

        @lru_cache(None)
        def solve(a, b):
            if a <= 0:
                if b <= 0:
                    return 0.5
                else:
                    return 1
            elif b <= 0:
                return 0
            
            return 0.25 * solve(a-100, b) + 0.25 * solve(a-75, b-25) + 0.25 * solve(a-50, b-50) + 0.25 * solve(a-25, b-75)
        return solve(n, n)
        
