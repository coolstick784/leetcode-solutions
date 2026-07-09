from collections import deque
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        diagonals = {} # x-y : deque
        for r, row in enumerate(grid):
            for c, el in enumerate(row):
                diag = r - c
                diagonals.setdefault(diag, []).append(el)
        for d in diagonals:
            diagonals[d].sort()
            if d >= 0:
                diagonals[d].reverse()
            diagonals[d] = deque(diagonals[d])
        for r, row in enumerate(grid):
            for c, el in enumerate(row):
                d = r - c
                grid[r][c] = diagonals[d].popleft()
        return grid

