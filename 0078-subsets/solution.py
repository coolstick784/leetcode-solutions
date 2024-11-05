class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        out = [[]]
        for n in nums:
            prev_out = out.copy()
            out_idx = 0
            while out_idx < len(out):
                prev_out.append(out[out_idx] + [n])
                out_idx += 1
            out = prev_out.copy()
        return out
                
