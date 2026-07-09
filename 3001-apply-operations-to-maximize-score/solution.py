# 1. list all primes
# 2. get the number of primes divisible by each n
# 3. figure out how many operations each number applies to on the right
# 4. figure out how many operations each number applies to on the left
# 5. multiply right * left to get total operations
# 6. do highest to lowest number in terms of ops until we hit k

from functools import lru_cache
is_prime = [True for _ in range(10**5+1)]
all_factors = [0 for _ in range(10**5+1)]
is_prime[0] = False
is_prime[1] = False
all_primes = []

for idx, p in enumerate(is_prime):
    if not p:
        continue
    all_factors[idx] = 1
    all_primes.append(idx)
    cur = idx + idx
    while cur <= 10**5:
        is_prime[cur] = False
        all_factors[cur] += 1
        cur += idx
MOD = 10**9+7
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
      
        num_primes = []
        
        for n in nums:
            
            num_primes.append(all_factors[n])
        num_right = [1 for _ in nums]
        num_left = [1 for _ in nums]
        stack = [] # idx, num primes
        for idx, n in enumerate(nums):
            while stack and num_primes[idx] > stack[-1][1]:
                pre_idx, _ = stack.pop()
                num_right[pre_idx] = idx - pre_idx
            stack.append((idx, num_primes[idx]))
        while stack:
            pre_idx, _ = stack.pop()
            num_right[pre_idx] = len(nums) - pre_idx
        
        stack = []
        for idx in range(len(nums)-1, -1, -1):
            while stack and num_primes[idx] >= stack[-1][1]:
                pre_idx, _ = stack.pop()
                num_left[pre_idx] = pre_idx - idx
            stack.append((idx, num_primes[idx]))
        while stack:
            pre_idx, _ = stack.pop()
            num_left[pre_idx] = pre_idx + 1
        

        total = [1 for _ in nums]
        
        for idx in range(len(nums)):
            total[idx] = num_left[idx] * num_right[idx]
        
        final = []
        for idx, n in enumerate(nums):
            final.append((n, total[idx]))
        
        final.sort(reverse=True)
        res = 1
        cur = 0
     

        def get_pow(n, p):
            return pow(n, p, MOD)

        for n, ops in final:
            print("n",n,"ops", ops)
           
            if cur + ops <= k:
                res *= get_pow(n, ops) % MOD

            else:
                res *=  get_pow(n, k-cur) % MOD
            res = res % MOD 
            cur += ops
            if cur >= k:
                break
        return res
            
        

        
