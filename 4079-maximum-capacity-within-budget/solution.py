import bisect
class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        highest = {}
        caps = {}
        all_costs = sorted(list(set(costs)))
        res = 0
        for idx, cost in enumerate(costs):
            cap = capacity[idx]
            caps.setdefault(cost, []).append((cap, idx))
        arr = []
        for idx, c in enumerate(all_costs):
            cur = caps[c]
            arr += cur
            arr.sort()
            arr.reverse()
            arr = arr[:2]
            if len(arr) == 1:
                arr.append((0, -1))

            highest[c] = arr.copy()

        for idx, c in enumerate(costs):
            cur = capacity[idx]
            if c >= budget:
                continue
            best_idx = bisect.bisect_left(all_costs, budget-c) - 1
            if best_idx >= 0:
                
                best = all_costs[best_idx]
   
                if highest[best][0][1] != idx:
                    cur += highest[best][0][0]
                else:
                    cur += highest[best][1][0]
            res = max(res, cur)
        return res
            
