class Solution:
    def stringHash(self, s: str, k: int) -> str:
        res = []
        su = 0
        for idx, ch in enumerate(s):
            su += ord(ch) - ord('a')
            if (idx+1) % k == 0:
                r = su % 26
                res.append(chr(ord('a') + r))
                su = 0
        return "".join(res)

