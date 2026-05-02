# at each point that we enter, we ether want the lowest neg number or highest pos number going into it
# then, at the end, we obviously want the highest product
# so two heaps, djikstra's algo, one for the lowest neg and one for the highest pos after exiting that number
# then, the highest positive at (m-1, n-1) is our ans

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        lowest_neg = [[None for _ in range(len(grid[0]))] for _ in range(len(grid))] 
        highest_pos = [[None for _ in range(len(grid[0]))] for _ in range(len(grid))] 
        self.has_zero = False

        def explore(start, row, col):

            if row >= len(grid) or col >= len(grid[0]):
                return

            if grid[row][col] == 0:

                self.has_zero = True
            if start < 0 and (lowest_neg[row][col] is None or start < lowest_neg[row][col]):
                lowest_neg[row][col] = start
            elif start > 0 and (highest_pos[row][col] is None or start > highest_pos[row][col]):
                highest_pos[row][col] = start
            else:
                return
            explore(start*grid[row][col], row+1, col)
            explore(start*grid[row][col], row, col+1)

        
        explore(1, 0, 0)
 
        end_val = grid[len(grid)-1][len(grid[0])-1]
        if end_val > 0 and highest_pos[len(grid)-1][len(grid[0]) - 1] is not None:
            return highest_pos[len(grid)-1][len(grid[0]) - 1] * end_val % (10**9+7)
        elif end_val < 0 and lowest_neg[len(grid)-1][len(grid[0]) - 1] is not None:
            return lowest_neg[len(grid)-1][len(grid[0]) - 1] * end_val % (10**9+7)
        elif self.has_zero:
            return 0
        else:
            return -1
