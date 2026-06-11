class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        res = []
        nums = [0] + nums
        for idx, n in enumerate(nums):
            n = abs(n)
            if nums[n] < 0:
                res.append(n)
            
            nums[n] *= -1
            
            
            

        return res
