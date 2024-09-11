class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        tot = []
        nums.sort()
        if len(nums) % 2 == 1:
            m = nums[int(len(nums)/2-0.5)]
        else:
            s = nums[int(len(nums)/2)]  + nums[int(len(nums)/2)-1]
            m = round(s/2)

        #m = round(sum(nums)/len(nums))
        tot.append(sum([abs(n-m) for n in nums]))
        return min(tot)

        
