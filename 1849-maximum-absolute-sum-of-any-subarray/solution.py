class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        neg = float('inf')
        pos = -float('inf')
        cur_neg = 0
        cur_pos = 0
        for idx, n in enumerate(nums):
            cur_neg += n
            cur_pos += n
            if cur_neg >= 0:
                cur_neg = 0
            if cur_pos <= 0:
                cur_pos = 0
            neg = min(cur_neg, neg)
            pos = max(cur_pos, pos)

        return max(abs(neg), pos)

