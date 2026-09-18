class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        res = []
        for _ in range(num):
            n = min(9, sum)
            sum -= n
            res.append(n)
        if sum > 0:
            return ""
        return "".join([str(n) for n in res])
