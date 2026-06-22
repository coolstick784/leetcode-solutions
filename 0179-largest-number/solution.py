from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(n) for n in nums]

        def compare(a, b):
            if a + b > b + a:
                return -1
            else:
                return 1
        res =  "".join(sorted(nums, key=cmp_to_key(compare))).lstrip("0")
        return "0" if not res else res
        
