from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        ctr = Counter(s)
        if not (ctr.get('a', 0) == ctr.get('b',0) and ctr.get('a',0) == ctr.get('c', 0)):
            return False
        q = deque()
        for idx, ch in enumerate(s):
            if ch == "a":
                q.append("bc")
            elif ch == "b":
                if not q:
                    return False
                if q[-1][0] == "b":
                    q.pop()
                    q.append("c")
                else:
                    return False
            elif ch == "c":
                if not q:
                    return False
                if q[-1][0] == "c":
                    q.pop()
                else:
                    return False

        return True if not q else False
