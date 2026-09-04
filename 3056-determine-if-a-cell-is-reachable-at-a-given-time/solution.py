class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        dist = max(abs(fx-sx), abs(fy-sy))
        if sx == fx and sy == fy and t == 1:
            return False
        return dist <= t
