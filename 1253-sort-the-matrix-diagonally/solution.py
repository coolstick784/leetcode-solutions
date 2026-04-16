# there is a matrix diagonal starting from each element in the top row as well as the leftmost column
# first, get a list of our start indices
# then, for each start index, go down 1 and right 1 until we can't anymore
# while we loop, add the value to the current arr, as well as the (row, col) index
#then, sort the array of values, and loop through the list of indices, setting that index's value to the sorted value at that index
# continue

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        starts = list(set([(0, col) for col in range(len(mat[0]))] + [(row, 0) for row in range(len(mat))]))
        res = mat.copy()
        for row, col in starts:
            indices = []
            vals = []
            cur_row = row
            cur_col = col
            while cur_row < len(mat) and cur_col < len(mat[0]):
                indices.append((cur_row, cur_col))
                vals.append(mat[cur_row][cur_col])
                cur_row += 1
                cur_col += 1
            vals.sort()

            for idx, (cur_row, cur_col) in enumerate(indices):
                res[cur_row][cur_col] = vals[idx]
        return res
            
        
