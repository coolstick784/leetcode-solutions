import heapq
from typing import List

class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        heap = [(prices[0], 1)]
        costs = {1: prices[0]}
        best_end = float("inf")

        while heap:
            cost, cur = heapq.heappop(heap)

            # skip stale heap entries
            if cost != costs.get(cur, float("inf")):
                continue

            # if paying at cur finishes, update answer
            if cur * 2 >= n:
                best_end = min(best_end, cost)
                continue

            for nxt in range(cur + 1, min(n, 2 * cur + 1) + 1):
                new_cost = cost + prices[nxt - 1]
                if new_cost < costs.get(nxt, float("inf")):
                    costs[nxt] = new_cost
                    heapq.heappush(heap, (new_cost, nxt))

        return best_end

