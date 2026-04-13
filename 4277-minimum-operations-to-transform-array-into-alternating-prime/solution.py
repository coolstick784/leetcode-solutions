# define the list of primes
# if it's prime and odd, add by 1
# if it's not prime and even, get the difference between that and the next highest prime using binary search

global primes
global primes_list
m = 200000
primes = [True for _ in range(m + 1)]
primes[0] = False
primes[1] = False
for n in range(2, int(m**0.5)+1):
    if primes[n]:
        cur = n + n
        while cur <= m:
            primes[cur] = False
            cur += n
primes_list = []
for idx, v in enumerate(primes):
    if v:
        primes_list.append(idx)
class Solution:
    def minOperations(self, nums: list[int]) -> int:

        global primes
        global primes_list
        res = 0
        for idx, n in enumerate(nums):
            if idx % 2 == 0 and primes[n] == False:
                next_prime = primes_list[bisect.bisect(primes_list, n)]

                res += (next_prime - n)
            elif idx % 2 == 1 and primes[n] == True:
                res += 1
                if n == 2:
                    res += 1
        return res

