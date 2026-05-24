class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
 

        def findLowest():
            left = 0
            right = len(nums) - 1
            while left <= right:
                med = (left + right) // 2
 
                if target > nums[med]:
                    left = med + 1
                elif nums[med] == target and (med == 0 or nums[med-1] < target):
                    return med
                else:
                    right = med - 1
            return -1

        def findHighest():
            left = 0
            right = len(nums) - 1
            while left <= right:
                med = (left + right) // 2
 
                if nums[med] > target:
                    right = med - 1
                elif nums[med] == target and (med == len(nums)-1 or nums[med+1] > target):
                    return med
                else:
                    left = med + 1
            return -1

        return [findLowest(), findHighest()]
