class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        res = 0
        as_s = str(x)
        for idx1, n1 in enumerate(nums):
            s = 0
            for idx2, n2 in enumerate(nums[idx1:]):
                s += n2
                s_s = str(s)
                if s_s[0] == as_s and s_s[-1] == as_s:
                    res += 1
        return res
