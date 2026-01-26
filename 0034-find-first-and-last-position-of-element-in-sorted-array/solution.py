class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        if len(nums) == 1 and nums[0] == target:
            return [0,0]
        def findFirstLeft(nums, target, cur_right, cur_left):

            
            while cur_left <= cur_right:
                print("finding left", cur_left, cur_right)
                cur_med = (cur_left + cur_right) // 2
                if nums[cur_med] == target and (cur_med == 0 or nums[cur_med-1] < target):
                    return cur_med
                elif nums[cur_med] > target:
                    cur_right = cur_med - 1
                elif nums[cur_med] < target :
                    cur_left = cur_med + 1
                else:
                    cur_right = cur_med - 1
            return cur_right
        def findLastRight(nums, target, cur_left, cur_right):

            
            while cur_left <= cur_right:
                print("finding right")
                cur_med = (cur_left + cur_right) // 2
                if nums[cur_med] == target and (cur_med == len(nums) - 1 or nums[cur_med+1] > target):
                    return cur_med
                elif nums[cur_med] > target:
                    cur_right = cur_med - 1
                elif nums[cur_med] < target:
                    cur_left = cur_med + 1
                else:
                    cur_left = cur_med + 1
            return cur_right
                

        while(left <= right):
            med = (left + right) // 2
            if nums[med] < target:
                left = med + 1
            elif nums[med] > target:
                right = med - 1
            elif nums[left] == target and nums[right] == target and (left == 0 or nums[left-1] < target) and (right == len(nums)-1 or nums[right+1] > target):
                return [left, right]
            else:
                print("finding")
                left = findFirstLeft(nums, target, med, left)
                right = findLastRight(nums, target, med, right)
                
                return [left, right]

        return [-1, -1]
