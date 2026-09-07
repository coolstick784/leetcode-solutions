class Solution:
    def minBishopMoves(self, source: list[int], target: list[int]) -> int:
        x1, y1 = source
        x2, y2 = target
        if abs(x2-x1) == abs(y2-y1):
            return 1
        p = set()
        for xc in range(-9, 9):

            nx = x1 + xc
            ny = y1 + xc
            if abs(nx-x2) == abs(ny-y2):
                
                return 2
        return -1
