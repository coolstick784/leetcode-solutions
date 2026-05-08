class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a, b):
            """
            Compute the greatest common divisor of two integers.
            
            args:
                a (int) : the first integer
                b (int) : the second integer
            
            return:
                int : the greatest common divisor of a and b.
            """
            max_val = min(a, b)
            res = 0
            for n in range(1, max_val+1):
                if (b % n == 0 or b == 0) and (a % n == 0 or a == 0):
                    res = n
            return res

        return gcd(min(nums), max(nums))
