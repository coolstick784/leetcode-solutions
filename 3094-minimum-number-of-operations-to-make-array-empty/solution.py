from collections import Counter
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ctr = Counter(nums)
        res = 0
        for n in ctr:
            ct = ctr[n]
            while ct > 1 and ct % 3 != 0:
                ct -= 2
                res += 1
            res += ct // 3

            if ct == 1:
                return -1
        return res
