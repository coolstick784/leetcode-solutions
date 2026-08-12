MOD = 10**9 + 7

class Solution:
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        n_right = n - pos - 1
        n_left = pos
        res = 0

        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD

        def combo(c, k):
            return (
                fact[c]
                * pow(fact[k], MOD - 2, MOD)
                * pow(fact[c - k], MOD - 2, MOD)
            ) % MOD

        for start in range(k // 2 + 1):
            end = k - start

            if start <= n_left and end <= n_right:
                res += combo(n_left, start) * combo(n_right, end) * 2

            if start <= n_right and end <= n_left and start != end:
                res += combo(n_right, start) * combo(n_left, end) * 2

            res %= MOD

        return res
