from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = {0: 1}   # prefix_sum -> how many times we've seen it
        prefix = 0
        res = 0

        for x in nums:
            prefix += x
            res += count.get(prefix - goal, 0)
            count[prefix] = 1 + count.get(prefix, 0)

        return res

