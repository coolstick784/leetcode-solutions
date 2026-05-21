class Solution:
    def largestEven(self, s: str) -> str:
        s = list(s)
        while s and s[-1] not in ["2", "4", "6", "8", "0"]:
            s.pop()
        return "".join(s)
