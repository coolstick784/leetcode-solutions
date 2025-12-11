class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, n in enumerate(nums):
            for idx2, j in enumerate(nums[idx+1:]):
                cur_idx = idx+idx2+1
                if n + j == target:
                    return [idx, cur_idx]

