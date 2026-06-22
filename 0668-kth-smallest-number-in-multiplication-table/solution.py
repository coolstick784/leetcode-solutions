# perfect squares are used once
# for all num <= min(m, n) that are not perfect squares, they are used twice
# everything else once

# first figure out what number it belonge to, then just multiply
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        left = 0
        right = m * n
        while left < right:
            med = (left + right) // 2
            low = math.floor(math.sqrt(med))
            cur = 0
            curM = m
            curN = n
            for num in range(1, min(low,m, n)+1):
                cur += max(0, min(curM-1, med // num - num )) + max(0, min(curN-1, med // num - num)) + 1

                curM -= 1
                curN -= 1
            if cur < k:
                left = med + 1
            else:
                right = med
        
        return left
            
            
