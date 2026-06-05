MOD = 10**9 + 7

class Solution:
    @lru_cache(None)
    def rearrangeSticks(self, n: int, k: int) -> int:
        if n == k:
            return 1
        if k == 0 or n == 0:
            return 0
        
        return (
            self.rearrangeSticks(n - 1, k - 1)
            + (n - 1) * self.rearrangeSticks(n - 1, k)
        ) % MOD
