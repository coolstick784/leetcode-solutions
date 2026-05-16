# first bit: every 2nd number starting at 1, it goes for 1
# second bit: every 4th number starting at 2, it goes for 2
# third bit, every 8th number starting at 4, it goes for 4
pows = [1]
for n in range(50):
    pows.append(2*pows[-1])
class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def calculateBit(n, bit_idx):
            start = pows[bit_idx-1]
            every = pows[bit_idx]
            n_groups = (n-start+1) // every
            extra = (n-start+1) % every
            return n_groups * start + min(extra, start)
        

        left = 1
        right = 10**15+1
        while left < right:
            med = (left + right) // 2
            cur =  0
            bit = x
            while bit < 50:
                cur += calculateBit(med, bit)
                bit += x
            if cur <= k:
                left = med + 1
            elif cur > k:
                right = med
        return left - 1
            


