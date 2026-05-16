# get the difference, make it absolute, then we need diff // limit numbers of the limit, then if the modulus is not 0 we need an extra

class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        cur_sum = sum(nums)
        diff = abs(cur_sum - goal)
        res = diff // limit
        if diff % limit != 0:
            res += 1
        return res

