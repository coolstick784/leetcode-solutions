class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        MAXBITS = 32

        def lis(nums):
            tails = []
            for num in nums:
                i = bisect_left(tails, num)
                if i == len(tails):
                    tails.append(num)
                else:
                    tails[i] = num
            return len(tails)

        result = 0
        for bit in range(MAXBITS):
            bitnums = [num for num in nums if (num >> bit) & 1]
            result = max(result, lis(bitnums))

        return result
