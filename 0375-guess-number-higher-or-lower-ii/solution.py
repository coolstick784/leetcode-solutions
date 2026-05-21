class Solution:
    def getMoneyAmount(self, n: int) -> int:
        
        @lru_cache(None)
        def solve(start, end):
            if start >= end:
                return 0
            
            best = float('inf')
            for guess in range(start, end+1):
                best = min(best, 
                    guess + 
                    max(solve(guess+1, end), solve(start, guess-1))
                )
            return best



        return solve(1, n)
