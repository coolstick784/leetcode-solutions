class Solution:
    def processStr(self, s: str) -> str:
        res = []
        letters = set([chr(ord('a') + n) for n in range(26)])
        for ch in s:
            if ch in letters:
                res.append(ch)
            elif ch == "*" and res:
                res.pop()
            elif ch == "#":
                res += res
            elif ch == "%":
                res.reverse()
        return "".join(res)


