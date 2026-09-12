class Solution:
    def minOperations(self, nums: List[int]) -> int:
        flips = [0 for _ in nums]
        n_flips = 0
        res = 0
        for idx, n in enumerate(nums):
            if n_flips % 2 == 1:
                n = -n + 1
            if n == 0:
                n_flips += 1
                if idx >= len(nums) - 2:
                    return -1 
                flips[idx+2] -= 1
                res += 1

            n_flips -= flips[idx]
        return res
