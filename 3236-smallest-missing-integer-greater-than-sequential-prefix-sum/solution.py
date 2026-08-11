class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        s = set(nums)

        cur_s = 0
        cur_l = 0
        for idx, n in enumerate(nums):
            if idx == 0 or n == nums[idx-1] + 1:
                cur_l += 1
                cur_s += n
            else:
                res = cur_s
                while res in s:
                    res += 1
                return res
        res = cur_s
        while res in s:
            res += 1
        return res
