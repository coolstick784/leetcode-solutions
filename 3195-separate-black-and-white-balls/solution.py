class Solution:
    def minimumSteps(self, s: str) -> int:
        cur = 0
        res = 0
        for idx, n in enumerate(s):
            if n == "1":
                cur += 1
            else:
                res += cur
        return res
