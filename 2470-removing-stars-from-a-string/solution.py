class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        for idx, ch in enumerate(s):
            if ch == "*":
                res.pop()
            else:
                res.append(ch)
        return "".join(res)
