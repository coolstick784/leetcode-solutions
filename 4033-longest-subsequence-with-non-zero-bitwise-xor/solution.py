class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        # HAS TO BE EITHER THE FULL LENGTH, OR LENGTH - 1
        # if the xors of [:-1] equal [-1], then its length - 1
        # otherwise its the length
        res = None
        if set(nums) == set([0]):
            return 0
        for idx, n in enumerate(nums[:-1]):
            if res == None:
                res = n
            else:
                res = res ^ n
        if res == nums[-1]:
            return len(nums) -1
        
        else:
            return len(nums)
            

        
