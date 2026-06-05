class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        
        sums = [0]
        for n in nums:
            sums.append(sums[-1] + n)
        @lru_cache(None)
        def solve(start, left):
            out = -float('inf')
            res = []

            if left == 0:
                return (0, [])
            if start >= len(nums):
                return (out, [])
            if start + k > len(nums):
                return (out, res)
           
            v2, s2 = solve(start+k, left-1)
            v2 += sums[start+k] - sums[start]
            if v2 > out:
                out = v2
                res = [start] + s2
            v1, s1 = solve(start+1, left)
            if v1 > out:
                out = v1
                res = s1.copy()
            print("start", start, "left", left, "out", out)
            return (out, res)
            

        return solve(0, 3)[1]
