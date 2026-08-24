primes = [True for _ in range(1001)]
primes[0] = False
primes[1] = False
for n, p in enumerate(primes):
    if not p:
        continue
    cur = n + n
    while cur <= 1000:
        primes[cur] = False
        cur += n
pre = [0]
for n, p in enumerate(primes):
    if n == 0:
        continue
    if p:
        pre.append(pre[-1] + n)
    else:
        pre.append(pre[-1])
print(pre)

class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        r = 0
        og = n
        digits = len(str(n)) - 1
        while n:
            digit = n % 10
            r += 10**(digits) * digit
            digits -= 1
            n //= 10
        print("r", r, "n", og)
        return pre[max(r, og)] - pre[min(r, og)-1]
