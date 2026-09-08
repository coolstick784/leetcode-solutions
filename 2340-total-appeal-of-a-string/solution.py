class Solution:
    def appealSum(self, s: str) -> int:
        last = {}
        res = 0
        prev = 0
        cur = 0
        for idx, ch in enumerate(s):
            if ch not in last:
                cur = (idx+1) + prev
            else:
                cur = prev + idx - last[ch]
            last[ch] = idx
            res += cur
            prev = cur
            cur = 0
        return res
