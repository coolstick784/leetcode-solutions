class Solution:
    def minOperations(self, k: int) -> int:
        left = 1
        right = k
        if k <= 1:
            return 0

        def solve(n):
            return math.ceil(k/n) - 1 + n - 1
        return min(solve(n) for n in range(1, k+1))
