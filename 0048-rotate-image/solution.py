# focus on the outermost part of the square
# go through each element in the first row, not including the last
# we'll iterate 4 times
# we'll have a temp var with the current number, the current row, col, and the next row, col
# 1. swap the temp and the next row, col
# 2. move on to the next row, col
# repeat
# once we hit the ned of the row - 1, 
# start at the next row, next col where row = col
# 0 -> 3
# center = 

# [0, 0] -> [0, 2] -> [2, 2] -> [2, 0] -> [0, 0]
#[1, -1] -> [1, 1] -> [-1, 1] -> [-1, -1] -> [1, -1]
# [x, y] -> [-y. x]
# get the distance from the center to calculate x and y
# center = [n//2-0.5, n//2-0.5]

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        max_col = len(matrix[0])-1
        max_r = len(matrix) - 1
        center = len(matrix) /2 -0.5
        for r, row in enumerate(matrix):
            for c, n in enumerate(row[r:max_col-r]):
                temp = n
                cur_r = r
                cur_c = c+r
                cur_x = center-cur_r

                cur_y = cur_c - center
              
                for _ in range(4):
                    cur_x, cur_y = -cur_y, cur_x
                    cur_r = int(center-cur_x)
                    cur_c = int(center+cur_y)
    
                    temp, matrix[cur_r][cur_c] = matrix[cur_r][cur_c], temp
            



