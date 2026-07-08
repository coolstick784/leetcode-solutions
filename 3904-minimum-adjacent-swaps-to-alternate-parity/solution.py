# can either go even -> odd or odd -> even
# so the first even goes to the first spot and so on

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        even_ctr = 0
        even_cost = 0
        odd_ctr = 0
        odd_cost = 0
        for idx, n in enumerate(nums):
            if n % 2 == 0:
                even_ctr += 1
                goal_idx = 0 + 2 * (even_ctr-1)
                even_cost += abs(idx-goal_idx)
                if goal_idx >= len(nums):
                    even_cost = float('inf')
            else:
                odd_ctr += 1
                goal_idx = 0 + 2 * (odd_ctr-1)
                odd_cost += abs(idx - goal_idx)
                if goal_idx >= len(nums):
                    even_cost = float('inf')


        if odd_ctr != math.ceil(len(nums)/2):
            odd_cost = float('inf')
        if even_ctr != math.ceil(len(nums)/2):
            even_cost = float('inf')
        res = min(odd_cost, even_cost)
        if res == float('inf'):
            res = -1
        return res
