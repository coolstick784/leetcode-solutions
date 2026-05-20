primes = [True for _ in range(10**6*5+1)]
primes[0] = False
primes[1] = False
l_primes = []
for idx, p in enumerate(primes):
    if p:
        l_primes.append(idx)
        cur = idx + idx
        while cur <= 10**6*5:
            primes[cur] = False
            cur += idx

class Solution:
    def countPrimes(self, n: int) -> int:
        return bisect.bisect_left(l_primes, n)
