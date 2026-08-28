class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(set(nums))
        res = 0
        for idx in range(len(nums)):
            ctr = {}
            for idx2 in range(idx, len(nums)):
                ch = nums[idx2]
                ctr[ch] = ctr.get(ch, 0) + 1
                if len(ctr) == n:
                    res += 1
        return res
