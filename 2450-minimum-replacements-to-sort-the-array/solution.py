# we obviously dont want to split the last element
# so we split the previous element just enough times to be <= the last and we'll have a current max

import math
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        curMax = nums[-1]
        cur_idx = len(nums) - 2
        res = 0
        while cur_idx >= 0:
            n = nums[cur_idx]
            numSplits = math.ceil(n / curMax) - 1
            res += numSplits
            curMax = n // (numSplits+1)


            cur_idx -= 1
        return res
