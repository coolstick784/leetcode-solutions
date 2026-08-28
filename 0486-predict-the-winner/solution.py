class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def solve(left, right):
            if left == right:
                return nums[left]
            diff_l = nums[left] - solve(left+1, right)
            diff_r = nums[right] - solve(left, right-1)
            return max(diff_l, diff_r)
                

        return solve(0, len(nums) - 1) >= 0
