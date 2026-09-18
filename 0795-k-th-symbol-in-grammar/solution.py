class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        @lru_cache(None)
        def solve(n, k):
            print(n, k)
            if n == 0:
                return 0
            if solve(n-1, math.ceil(k/2)) == 0 and k % 2 == 0:
                return 1
            if solve(n-1, math.ceil(k/2)) == 1 and k % 2 == 1:
                return 1
            return 0

        return solve(n, k)
