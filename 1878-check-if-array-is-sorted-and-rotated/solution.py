# it can have up to 1 point where n1 > n2, but then nums[-1] must be < nums[0]
class Solution:
    def check(self, nums: List[int]) -> bool:
        point = False
        if nums[-1] > nums[0]:
            point = True
        for idx, n in enumerate(nums):
            if idx == 0:
                continue
            if n < nums[idx-1]:
                if point:
                    return False
                point = True
        return True
