class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        pot = [0] + sorted(cuts) + [n]
        @lru_cache(None)
        def dfs(i, j):
            if j - i <= 1:
                return 0
            out = []
            for k in range(i+1, j):
                out.append(pot[j] - pot[i] + dfs(i, k) + dfs(k, j))

            return min(out)



        return dfs(0, len(pot)-1)
