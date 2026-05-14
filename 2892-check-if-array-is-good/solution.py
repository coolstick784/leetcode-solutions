# counter
# from 1 and going up, if the count of that number is 1, keep going
#otherwise, if the count is 0, return False
# if the count is 2, return true
# is it equal to its idx + 1?
# if so, move forward
# if not, is it equal to its index AND is it the last number?
# if so, return True, otherwise, return False
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        for idx, n in enumerate(nums):
            if n == idx + 1:
                continue
            if n == (idx) and idx == len(nums) - 1:
                return True
            return False


        return False

