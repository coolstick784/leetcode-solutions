# loop through every number in nums and see if it is a valid start idx
# if it's already in another set, we can ignore it -- it is circular, so it doesn't help to explore something already explored
# if we look through it, we want to find the longest length, and add each number to the explored set

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        explored = set()
        res = 0
        for idx, n in enumerate(nums):
            if idx not in explored:
                cur_set = set()
                cur_idx = idx
                cur_val = nums[cur_idx]
                while cur_val not in cur_set:

                    cur_set.add(cur_val)
                    explored.add(cur_idx)
                    res = max(res, len(cur_set))
                    cur_idx = cur_val
                    cur_val = nums[cur_idx]


        return res
