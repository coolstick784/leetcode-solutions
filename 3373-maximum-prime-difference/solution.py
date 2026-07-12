primes = [True for _ in range(101)]
primes[0] = False
primes[1] = False
for idx in range(1, 101):
    if primes[idx]:
        cur = idx + idx
        while cur <= 100:
            
            primes[cur] = False
            cur += idx
class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        left = None
        right = None
        for idx, n in enumerate(nums):
            if primes[n]:
                right = idx
                if left is None:
                    left = idx

        return right - left
        
