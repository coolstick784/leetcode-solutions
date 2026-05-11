class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            cur = []
            while n > 0:
                cur.append(n % 10)
                n = n // 10
            cur.reverse()
            res += cur
        return res
