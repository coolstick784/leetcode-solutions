pows = [1]
for _ in range(32):
    pows.append(2*pows[-1])
class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        total = 0
        for p in pows:
            for n in nums:
                if n & p:
                    total += p
                    break
        return total
