class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @lru_cache(None)
        def solve(p, cur):
            if cur == 0:
                return 0
            if p >= len(piles):
                return 0
            out = 0
            s = 0
            out = max(out, solve(p+1, cur))
            for idx in range(min(cur,len(piles[p]) )):
                s += piles[p][idx]
                out = max(out, s + solve(p+1, cur-idx-1))

            return out


        return solve(0, k)


