class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        factors = []
        for n in range(1, len(s)):
            if len(s) % n == 0:
                factors.append((n,len(s)//n))
        for factor in factors:
   
            start = s[:factor[0]]
            mul = factor[1]

            if start * mul == s:
                return True
        return False
