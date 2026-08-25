class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s2 = list(s2)
        s1.sort()
        s2.sort()
        up = True
        down = True
        for idx, ch in enumerate(s1):
            if ch > s2[idx]:
                down = False
            elif ch < s2[idx]:
                up = False
        return up or down
