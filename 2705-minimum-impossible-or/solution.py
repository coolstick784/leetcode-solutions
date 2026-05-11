# we want to know every bit that can be turned out, then turn the smallest bit to 1
pows = [1]
for _ in range(32):
    pows.append(2*pows[-1])
class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        bits = [0 for _ in range(32)]
        set_n = set(nums)

        for p in pows:
            if p not in set_n:
                return p
