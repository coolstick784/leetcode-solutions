class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        cur = 0
        for n in nums:
            cur = cur ^ n
        return cur
