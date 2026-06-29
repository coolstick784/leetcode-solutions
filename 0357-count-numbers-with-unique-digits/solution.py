class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:

        if n == 0:
            return 1
        
        return 9 * math.factorial(9) // math.factorial(9-n+1) + self.countNumbersWithUniqueDigits(n-1)
