class Solution:
    def maxScore(self, nums: List[int]) -> int:
        def lcm(l1):


            out = 1
            for n in l1:
                cur = out
                while out % n != 0:
                    out += cur
            return out
        
        def gcd(l1):
            multiples = set([n for n in range(1, 31)])

            for n in l1:
                for i in range(1, 31):
                    if n % i != 0:
                        if i in multiples:
                            multiples.remove(i)


            return max(multiples)
        
        if len(nums) == 1:
            return nums[0] **2
        
        res = -float('inf')
        nums.sort()
        res = max(res, lcm(nums) * gcd(nums))
        for idx, n in enumerate(nums):
            new = nums[:idx] + nums[idx+1:]
            print("new", new, "lcm", lcm(new), "gcd", gcd(new))
            res = max(res, lcm(new) * gcd(new))
        return res
