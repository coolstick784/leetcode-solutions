

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:

        @lru_cache(None)
        def maxJumps(idx):
            if idx == len(nums) - 1:
                return 0
            n = nums[idx]
            out = [-float('inf')]
            for idx2 in range(idx+1, len(nums)):
                n2 = nums[idx2]
                if n2-n >= -target and n2-n <= target:
                    out.append(maxJumps(idx2))
            return 1+max(out)
        
        res= maxJumps(0)
        if res == -float('inf'):
            return -1
        return res
        
