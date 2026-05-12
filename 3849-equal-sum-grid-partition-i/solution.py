# we want the sum of each row and column, as well as the overall sum
# for each possible cut, we want to know the sum of rows above and below it
# then, if the usm of rows above (or cols to the left) = 1/2 the toal, return true
# after we've looped through everything, if we haven't found a sol, return False

# row sums = [5, 5]
# col sums = [2, 3]
# total = 10
# 5 = 5
# return True

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        row_sums = [0 for _ in grid]
        col_sums = [0 for _ in grid[0]]
        for r, row in enumerate(grid):
            for c, el in enumerate(row):
                row_sums[r] += el
                col_sums[c] += el
        print("row sums", col_sums)
        total = sum(row_sums)
        cur = 0
        rest = total
        for cur_sum in row_sums:
            cur += cur_sum
            rest -= cur_sum
            if cur == rest:
                return True
        cur = 0
        rest = total
        for cur_sum in col_sums:
            cur += cur_sum
            rest -= cur_sum
            
            if cur == rest:
                return True
        return False
            
