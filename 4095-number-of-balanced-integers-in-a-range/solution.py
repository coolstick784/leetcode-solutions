from collections import deque
class Solution:
    def countBalanced(self, low: int, high: int) -> int:

        def solve_n(n):
            digits_left = len(str(n))
        
            excess = 0
 
            return solve(digits_left, excess, n, 0)
        @lru_cache(None)
        def solve(digits_left,  excess, n, idx, prev_max = True):

            
            if digits_left == 0 and excess == 0:
                return 1
            elif digits_left == 0:
                return 0
            out = 0
            for i in range(10):
                if prev_max and i == int(str(n)[idx]):
                    out += solve(digits_left-1, -1 * (excess-i), n, idx+1, True)
                    break
                else:
                    out += solve(digits_left-1, -1 * (excess-i), n, idx+1, False)
            return out

        

        return solve_n(high) - solve_n(low-1)
