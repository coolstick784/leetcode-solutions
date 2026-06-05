import math
class Solution:
    def countOrders(self, n: int) -> int:
        total = math.factorial(n*2)
        return (total // 2 ** n) % (10**9+7)

