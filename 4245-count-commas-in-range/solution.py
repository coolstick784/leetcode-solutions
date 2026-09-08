class Solution:
    def countCommas(self, n: int) -> int:
        res = 0
        if n >= 1000:
            res += (n-1000 + 1)
        return res
