class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque([0])
        minVal = minJump
        maxVal = min(maxJump, len(s) - 1)
        for idx, ch in enumerate(s):
            while idx > maxVal and q:
                q.popleft()
                if q:
                    minVal = q[0] + minJump
                    maxVal = min(q[0] + maxJump, len(s) - 1)
            if ch == "0":
                if idx >= minVal and idx <= maxVal:
                    q.append(idx)
                    if idx == len(s) -1:
                        return True
        return False

