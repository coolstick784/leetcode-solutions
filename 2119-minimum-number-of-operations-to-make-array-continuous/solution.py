import bisect
# how many numbers do we have to insert if the number is the minimum or the maximum?
# add 1 for each number in the range that is duplicated
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums.sort()

        cur = 0
        duplicates = {}
        for idx, n in enumerate(nums):
            if idx == 0:
                continue
            if n == nums[idx-1]:
                cur += 1
            duplicates[idx] = cur
        res = float('inf')
        for idx, n in enumerate(nums):
            right = n + len(nums) - 1
            left = n - len(nums) + 1
            right_idx = bisect.bisect(nums, right) - 1
            
            between = right_idx - idx + 1 - (duplicates.get(right_idx, 0) - duplicates.get(idx-1, 0))
            res = min(res, len(nums) - between)

            left_idx = bisect.bisect_left(nums, left) - 1
            between = idx - left_idx - (duplicates.get(idx, 0) - duplicates.get(left_idx, 0))
            res = min(res, len(nums) - between )
        return res  

