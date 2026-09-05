class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []
        for i1, n1 in enumerate(nums):
            cur = 0
            for i2, n2 in enumerate(nums[i1:]):
                cur += n2
                sums.append(cur)
        sums.sort()
        return sum(sums[left-1:right]) % (10**9 + 7)
