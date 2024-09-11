class Solution:
    def countOdds(self, low: int, high: int) -> int:
        tot = 0
        if high % 2 == 1:
            high += 1
        if low % 2 == 1:
            low -= 1
        tot += (high - low)//2
        return tot
