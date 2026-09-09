class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        top = float('inf')
        bottom = -float('inf')
        left = float('inf')
        right = -float('inf')
        for r, row in enumerate(grid):
            for c, el in enumerate(row):
                if el == 0:
                    continue
                top = min(top, r)
                bottom = max(bottom, r)
                left = min(left, c)
                right = max(right, c)


        if top == float('inf'):
            return 0
        return (bottom - top + 1) * (right - left + 1)
