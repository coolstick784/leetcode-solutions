class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        l = len(nums[0])
        nums = [int(n) for n in nums]
        digits = {}
        for t in range(l, 0, -1):
            cur_ten = 10 ** (t - 1)
            digits[t] = []
            for idx, n in enumerate(nums):
                digits[t].append((n, idx))
                if n >= cur_ten:
                    nums[idx] = nums[idx] % cur_ten
        for t in range(l, 0, -1):
            digits[t].sort()
        res = []
       
        
        for k, trim in queries:
            
            
            res.append(digits[trim][k-1][1])
        return res
