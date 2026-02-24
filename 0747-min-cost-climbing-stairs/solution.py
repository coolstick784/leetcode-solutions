class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_costs = []
        for idx, n in enumerate(cost):
            if idx == 0:
                min_costs.append(n)
            elif idx == 1:
                min_costs.append(n)
            else:
                min_costs.append(min(min_costs[-1], min_costs[-2]) + n)
        return min(min_costs[-1], min_costs[-2])
