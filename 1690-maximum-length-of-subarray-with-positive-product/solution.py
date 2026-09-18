class Solution:
    def getMaxLen(self, nums: list[int]) -> int:
        res = 0
        max_neg = 0
        max_pos = 0
        for idx, n in enumerate(nums):
            if n > 0:
                if max_neg:
                    max_neg += 1
                max_pos += 1
            elif n == 0:
                max_neg = 0
                max_pos = 0
            else:
                old_pos = max_pos
                if max_neg:
                    max_pos = max_neg + 1
                else:
                    max_pos = 0
                if old_pos:
                    max_neg = old_pos + 1
                else:
                    max_neg = 1
            res = max(res, max_pos)
            print("idx", idx, "max neg", max_neg, "max pos", max_pos)
        return res
