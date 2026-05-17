# sum before, sum after
# average it out
# get the min

# sb = [2, 7, 10 19, 24, 27]
# sa = [25, 20, 17, 8, 3, 0]
# (2/1) 

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        sum_before = []
        cur = 0
        for n in nums:
            cur += n
            sum_before.append(cur)
        sum_after = []
        cur = 0
        for n in nums[::-1]:
            
            sum_after.append(cur)
            cur += n
        sum_after.reverse()
        res = (-1, float('inf'))
        for idx in range(len(nums)):
            ab = math.floor(sum_before[idx] / (idx+1))
            aa = 0
            if idx != len(nums) - 1:
                aa = math.floor(sum_after[idx] / (len(nums) - idx - 1))
            if abs(ab-aa) < res[1]:
                res = (idx, abs(ab-aa)) 

        return res[0]
