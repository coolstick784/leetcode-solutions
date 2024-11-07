class Solution(object):
    def search(self, nums, target, idx= 0):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        med = len(nums) // 2
        if len(nums) == 1 and target != nums[0]:
            return -1
        if target > nums[med]:
            return self.search(nums[med:], target, idx+med)
        elif target < nums[med]:
            return self.search(nums[:med], target, idx)
        else:
            return idx + med
        
