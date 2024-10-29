class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        cur_max = min(nums)
        for idx, n in enumerate(nums):
            total += n
            if total > cur_max:
                cur_max = total
            total = max(0, total)
        return cur_max
            
