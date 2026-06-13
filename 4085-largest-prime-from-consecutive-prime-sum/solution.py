out = []
total = []
primes = [True for _ in range(10**6)]
MAX = 10**6
for idx, p in enumerate(primes):
    if idx == 0:
        primes[idx] = False
        continue
    if idx == 1:
        primes[idx] = False
        continue
    if p:
        cur = idx + idx
        while cur < MAX:
            primes[cur] = False
            cur += idx
        total.append(idx)
cur = 0
out = [0]
for n in total:
    cur += n
    if cur >= MAX:
        break
    if primes[cur]:
        out.append(cur)

class Solution:
    def largestPrime(self, n: int) -> int:
        return out[bisect.bisect_right(out, n)-1] 
        
