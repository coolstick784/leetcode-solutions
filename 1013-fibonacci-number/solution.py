class Solution:
    def fib(self, n: int) -> int:
        def helper(n):
            if n == 0:
                return (0, 1)
            a, b = helper(n//2)
            c = a*(2*b-a)
            d = a*a+b*b
            if n % 2 == 0:
                return (c, d)
            return (d, c+d)
        return helper(n)[0]
