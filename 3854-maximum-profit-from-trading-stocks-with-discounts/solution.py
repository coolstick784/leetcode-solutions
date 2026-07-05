from functools import lru_cache
from typing import List

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        
        bosses = {}

        for b, e in hierarchy:
            bosses.setdefault(b, []).append(e)

        def merge(a, b):
            out = {}

            for cost1, profit1 in a.items():
                for cost2, profit2 in b.items():
                    new_cost = cost1 + cost2

                    if new_cost <= budget:
                        out[new_cost] = max(
                            out.get(new_cost, -float("inf")),
                            profit1 + profit2
                        )

            return out

        @lru_cache(None)
        def solve(e, half_off):
            children = bosses.get(e, [])

            # Option 1: don't buy employee e
            no_buy = {0: 0}

            for emp in children:
                child_best = solve(emp, False)
                no_buy = merge(no_buy, child_best)

            # Option 2: buy employee e
            price = present[e - 1] // 2 if half_off else present[e - 1]
            profit = future[e - 1] - price

            buy = {}

            if price <= budget:
                buy = {price: profit}

                for emp in children:
                    child_best = solve(emp, True)
                    buy = merge(buy, child_best)

            # Combine buy and no_buy
            best = no_buy.copy()

            for cost, val in buy.items():
                best[cost] = max(best.get(cost, -float("inf")), val)

            return best

        ans = solve(1, False)
        return max(ans.values())
