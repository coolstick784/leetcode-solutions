class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        mn = nums[0]
        
        mx_idx = len(nums) - 1
        res = 0
        mx = float('inf')
        while mx_idx >= 0:
            mx = nums[mx_idx] + res
            
            res += mx - mn
            mn = mx
            mx_idx -= 1
        return res
            

