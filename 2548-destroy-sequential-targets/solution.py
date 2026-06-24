class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        nums.sort()
        mx = 1
        res = float('inf')
        mod = {}
        for idx, n in enumerate(nums):
            cur = n % space
            mod.setdefault(cur, []).append(idx)
        for n in mod:
            if len(mod[n]) > mx:
                mx = len(mod[n])
                res = nums[mod[n][0]]
            elif len(mod[n]) == mx:
                res = min(res, nums[mod[n][0]])
        return res
