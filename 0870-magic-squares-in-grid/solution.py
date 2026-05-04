# at each potential upper left value, we want to know:
# the sum of the first row, second row, and third row
# the sum of the first col, second col, and third col
# the sum of both diagonals
# the 

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
        res = 0
        for r, row in enumerate(grid):
            for c, el in enumerate(row):

                if r > len(grid) -3 or c > len(grid[0]) - 3:
                    continue
                r1 = el + grid[r][c+1] + grid[r][c+2]
                r2 = grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2]
                r3 = grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2]
                c1 =grid[r][c] + grid[r+1][c] + grid[r+2][c]
                c2 = grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1]
                c3 = grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2]
                d1 = grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2]
                d2 = grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c]
                if not (r1 == r2 and r2 == r3 and r3 == c1 and c2 == c3 and c3 == d1 and d1 == d2):
                    continue
                nums = [el, grid[r+1][c], grid[r+2][c], grid[r][c+1], grid[r][c+2], grid[r+1][c+1], grid[r+1][c+2], grid[r+2][c+1], grid[r+2][c+2]]
                if set(nums) != s:
                    continue
                res += 1
        return res
