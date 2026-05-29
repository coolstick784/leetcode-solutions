class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7

        @lru_cache(None)
        def solve(cur_n, mn, idx):
            if idx == len(group):
                return 1 if mn == 0 else 0

            out = solve(cur_n, mn, idx + 1)

            if cur_n >= group[idx]:
                out += solve(
                    cur_n - group[idx],
                    max(mn - profit[idx], 0),
                    idx + 1
                )

            return out % MOD

        return solve(n, minProfit, 0)
