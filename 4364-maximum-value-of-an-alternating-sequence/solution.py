class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        if n == 1:
            return s
        
        n2 = n // 2
        s -= (n2 - 1)
        s += n2 * m
        return s
 
