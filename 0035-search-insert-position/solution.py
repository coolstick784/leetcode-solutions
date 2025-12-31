class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
       cur_idx = int(len(nums) / 2)
       forward_backward = "none"
       while True:
            if nums == [] and forward_backward != "forward":
                return cur_idx
            elif nums == []:
                return cur_idx + 1
            mid_idx = int(len(nums) / 2)
            if forward_backward == "forward":
                cur_idx += mid_idx + 1
            elif forward_backward == "backward":
                cur_idx -= (len(nums) - mid_idx)
            print(nums)
            print("cur_idx", cur_idx)
            print("mid_idx", mid_idx)

            print("current middle", nums[mid_idx])

            if len(nums) == 1:
                if target <= nums[0]:
                    return cur_idx
                elif target == nums[0]:
                    return cur_idx
                else:
                    return cur_idx + 1
            
            if target > nums[mid_idx]:
                nums = nums[mid_idx + 1:]
                forward_backward = "forward"
            elif target == nums[mid_idx]:
                return cur_idx
            else:
                nums = nums[:mid_idx]
                forward_backward = "backward"
