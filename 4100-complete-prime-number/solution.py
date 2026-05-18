primes = [True for _ in range(10**7+1)]
primes[0] = False
primes[1] = False
l_primes = []
for idx, p in enumerate(primes):
    if p:
        l_primes.append(idx)
        cur = idx + idx
        while cur <= (10**4):
            primes[cur] = False
            cur += idx

class Solution:
    def completePrime(self, num: int) -> bool:
        s = str(num)
        for idx in range(len(s)+1):
            pre = s[:idx]
            suf = s[idx:] 
            if pre != '':
                i = int(pre)
                if i <= 10**4 and not primes[i]:
                    return False
                elif i > 10**4:
                    for p in l_primes:
                        if i % p == 0:
                            return False
                        if p >= math.sqrt(i):
                            break
            if suf != '':
                i = int(suf)
                if i <= 10**4 and not primes[i]:
                    return False
                elif i > 10**4:
                    for p in l_primes:
                        if i % p == 0:
                            return False
                        if p >= math.sqrt(i):
                            break
        return True
