# we want the max of everything to the left of it, including the number
# we want the max of everythign to the right of it, not including the number
# starting at the left, if max(left) <= max(right), return that index

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        max_l = [None for _ in nums]
        cur_max = -float('inf')
        for idx, n in enumerate(nums):
            cur_max = max(cur_max, n)
            max_l[idx] = cur_max
        cur_min = float('inf')
        min_r = [None for _ in nums]
        for idx in range(len(nums)-1, -1, -1):
            n = nums[idx]
            if idx == len(nums) - 1:
                min_r[idx] = float('inf')
            else:
                min_r[idx] = cur_min
            cur_min = min(cur_min, n)

        for idx, n in enumerate(nums):
            if max_l[idx] <= min_r[idx]:
                return idx+1
