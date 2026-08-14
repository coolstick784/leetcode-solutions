class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @lru_cache(None)
        def solve(n):
            if n == 1:
                return 0
            if n % 2 == 0:
                return solve(n // 2) + 1
            return solve(n*3+1) + 1
        res = []
        for n in range(lo, hi+1):
            res.append((solve(n), n))
        res.sort()
        print(res)
        return res[k-1][1]
