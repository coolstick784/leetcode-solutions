class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])

        # width[r][c] = number of consecutive 1s ending at (r, c) from the left
        width = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1:
                    if c == 0:
                        width[r][c] = 1
                    else:
                        width[r][c] = width[r][c - 1] + 1

        res = 0

        # Treat each cell as the bottom-right corner
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    continue

                min_width = width[r][c]

                # Go upward and see how wide the rectangle can stay
                for up in range(r, -1, -1):
                    if width[up][c] == 0:
                        break

                    min_width = min(min_width, width[up][c])
                    res += min_width

        return res
