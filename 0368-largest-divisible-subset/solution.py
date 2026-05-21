class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        nums.sort()

        self.max = 1
        res= [nums[0]]
        @lru_cache(None)
        def solve(i):
            out = [nums[i]]
            for new_idx in range(i+1, len(nums)):
                if nums[new_idx] % nums[i] == 0:
                    cur = [nums[i]] + solve(new_idx)
                    if len(cur) > len(out):
                        out = cur.copy()

            return out
        for idx, n in enumerate(nums):
            if len(solve(idx)) > self.max:
                self.max = len(solve(idx))
                res = solve(idx)
        return res
