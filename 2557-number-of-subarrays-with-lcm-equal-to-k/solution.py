class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        

        @lru_cache(None)
        def getDivisors(num):
            return set([n for n in range(1, num+1) if num % n == 0])
        @lru_cache(None)
        def lcm(a, b):
            a, b = max(a, b), min(a,b)
            c = a
            while c % b != 0:
                c += a
            return c
        @lru_cache(None)
        def union(s, target):
            divisors = getDivisors(target)

            return [n for n in divisors if lcm(s, n) == target]
        # we want whatever's in divisors but not in the multiples of start
        @lru_cache(None)
        def solve(start, goal):
            if start >= len(nums):
                return 0
            n = nums[start]
            if goal % n != 0:
                return 0
            if goal == n:
                out = 1
                
                for d in getDivisors(n):
                    out += solve(start+1, d)

                return out 
            out = 0
            print("start", n, "Goal", goal, "union", union(n, goal))
            for u in union(n, goal):
                
                out += solve(start+1, u)
            
            return out
            

        return sum([solve(i, k) for i, _ in enumerate(nums)])
