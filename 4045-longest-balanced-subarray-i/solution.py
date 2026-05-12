class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        res = 0
        for left, n in enumerate(nums):
            even = set([])
            odd = set([])
            for right in range(left, len(nums)):
                n2 = nums[right]
                if n2 % 2 == 1:
                    odd.add(n2)
                else:
                    even.add(n2)
                if len(even) == len(odd):
                    res = max(res, right-left+1)
        return res


