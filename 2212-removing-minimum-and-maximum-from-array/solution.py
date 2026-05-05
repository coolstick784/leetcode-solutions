# we can either delete max and min from the left, max from the left and min from the right, max from the right and min from the left, or both from the right
# if max idx < min idx obviously we would need to remove max from the left and min from the right and vice versa

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_val = min(nums)
        max_val = max(nums)
        min_idx = nums.index(min_val)
        max_idx = nums.index(max_val)
        from_left = max(min_idx, max_idx) + 1
        from_right = max(len(nums)-min_idx, len(nums)-max_idx)
        if min_idx < max_idx:
            from_both = min_idx+1 + (len(nums) - max_idx)
        else:
            from_both = max_idx + 1 + (len(nums)-min_idx)

        return min([from_left,from_right,from_both])
        
