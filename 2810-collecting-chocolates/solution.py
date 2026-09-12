class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        best_per = {}
        for idx, n in enumerate(nums):
            best_per[idx] = n

        l = len(nums)
        cur_cost = sum(nums)
        total_best = cur_cost
        for k in range(l):
            if k > 0:
                cur_cost += x
            for idx, n in enumerate(nums):

                cost = nums[(idx + k) % l]
                if cost < best_per[idx]:
                    cur_cost -= (best_per[idx] - cost)
                    best_per[idx] = cost
            total_best = min(total_best, cur_cost)
        return total_best
