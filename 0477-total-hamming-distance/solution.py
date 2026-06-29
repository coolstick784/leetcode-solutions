pows = [2**n for n in range(33)]
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        bits_on = [0 for _ in range(33)]
        bits_off = [0 for _ in range(33)]
        for idx, n in enumerate(nums):
            for i, p in enumerate(pows):
                if n & p:
                    bits_on[i] += 1
                else:
                    bits_off[i] += 1

        res = 0
        for i in range(32):
            res += bits_on[i] * bits_off[i]
        return res
