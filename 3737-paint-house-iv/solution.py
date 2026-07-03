from functools import lru_cache
class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        dp = {} # best for 
        @lru_cache(None)
        def solve(e, prev_left = None, prev_right = None):
            if e >= n // 2:
                return 0
            combos = [(1, 2), (1, 3), (2, 3), (3, 1), (3, 2), (2, 1)]
            res = float('inf')
            for left, right in combos:
                if left == prev_left or right == prev_right:
                    continue
                res = min(res, cost[e][left-1] + cost[n-e-1][right-1] + solve(e+1, left, right))
                
            return res
        return solve(0)
