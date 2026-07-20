class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        

        @lru_cache(None)
        def solve(target):
            if target == 0:
                return 1
            if target < 0:
                return 0
            out = 0
            for idx, n in enumerate(nums):
                out += solve(target-n)
            return out
            
        
        return solve(target)
