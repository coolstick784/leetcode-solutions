# fill in row by row
# it's the prev row + the number of Xs so far in that row, including the current elemtn

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        res = 0
        cur_x = 0
        cur_y = 0
        num_x = [[0 for _ in grid[0]] for _ in grid]
        num_y = [[0 for _ in grid[0]] for _ in grid]
        for r, row in enumerate(grid):
            for c, el in enumerate(row):
                if r == 0:
                    prev_x_row = 0
                    prev_y_row = 0
                else:
                    prev_x_row = num_x[r-1][c]
                    prev_y_row = num_y[r-1][c]
                if c == 0:
                    cur_x = 0
                    cur_y = 0
                if el == 'X':
                    cur_x += 1
                elif el == 'Y':
                    cur_y += 1
                x_val = prev_x_row + cur_x
                y_val = prev_y_row + cur_y
                num_x[r][c] = x_val
                num_y[r][c] = y_val
                if x_val == y_val and x_val != 0:
                    res += 1
        return res


        
