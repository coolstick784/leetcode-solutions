class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = float('inf')
        for n in nums:
            cur = 0
            cn = n
            while cn > 0:
                cur += cn % 10
                cn //= 10
            res = min(res, cur)
        return res
    
