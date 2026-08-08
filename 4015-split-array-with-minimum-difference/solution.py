class Solution:
    def splitArray(self, nums: List[int]) -> int:
        lsum = 0
        rsum = 0
        lsum2 = 0
        rsum2 = 0
        for idx, n in enumerate(nums):
            if idx == 0 or (rsum == 0 and n > nums[idx-1]):
                lsum += n
                lsum2 += n
            elif n < nums[idx-1] or (n == nums[idx-1] and rsum == 0):
                if rsum == 0 and n < nums[idx-1]:
                    lsum2 = lsum - nums[idx-1]
                    rsum2 = nums[idx-1]
                rsum += n
                rsum2 += n
        
            else:
                return -1
        if rsum == 0:
            lsum2 = lsum - nums[-1] 
            rsum2 = nums[-1]
        
        res = abs(lsum - rsum)
        res = min(res, abs(lsum2 - rsum2))
        return res
