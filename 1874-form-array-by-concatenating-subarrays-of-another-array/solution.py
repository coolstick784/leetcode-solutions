class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        subarr_idx = 0
        groups_idx = 0
        left = 0
        right = 0
        n_groups = len(groups)
        len_group = len(groups[groups_idx])
        len_nums = len(nums)

        while left < len_nums and right < len_nums:
            l = nums[left]
            r = nums[right]
            comp = groups[groups_idx][subarr_idx]
            if r != comp:
                
                left += 1
                right = left
                subarr_idx = 0
            elif subarr_idx == len_group - 1:
                groups_idx += 1
                right += 1
                subarr_idx = 0
                left = right
                if groups_idx == n_groups:
                    return True
                len_group = len(groups[groups_idx])
            else:
                subarr_idx += 1
                right += 1


        return False
                




        
