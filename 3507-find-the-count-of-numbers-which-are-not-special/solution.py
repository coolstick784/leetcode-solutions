import math

class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        MOD = 10**9 + 7  # not needed here, just habit

        cur = r - l + 1

        low = math.isqrt(l)
        if low * low < l:
            low += 1
        high = math.isqrt(r)

        if high < 2 or low > high:
            return cur  # no prime squares possible

        # Sieve primes up to high
        is_prime = [True] * (high + 1)
        is_prime[0] = is_prime[1] = False

        limit = math.isqrt(high)
        for p in range(2, limit + 1):
            if is_prime[p]:
                step_start = p * p
                for x in range(step_start, high + 1, p):
                    is_prime[x] = False

        special = sum(is_prime[low:high + 1])  # primes p where p^2 in [l, r]
        return cur - special

