# make each possible cut that has an apple either in the left or over it
# for each possible cut, add that solution to our sum
# so we have a function, solve, that will take in top row, leftmost col, and k left
# if k left == 0 and there is at least one apple in the remaining, return 1
# otherwise, if k left ==0, return 0


# basically we want to ask:
# for each potential horizontal or vertical split, will there be at least one apple in each section?
# if so, return the number of splits possible for k-1 with the right or lower split

# to check if an apple is in the right/lower split, we can create an num_lower_right grid for each el that has the number of apples lower/to the right of it
# then, we do num lower (original) - num lower (new split) to get num apples in the left/upper
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:

        grid = [[0 for _ in range(len(pizza[0]))] for _ in pizza]
        for row, word in enumerate(pizza):

            for col, ch in enumerate(word):

                if ch == "A":

                    grid[row][col] = 1
        num_lower_right = [[0 for _ in range(len(pizza[0]))] for _ in pizza] # if there exists an apple either below, to the right, or both
        num_right = [[0 for _ in range(len(pizza[0]))] for _ in pizza] # the number of apples directly right, not including it
        num_lower = [[0 for _ in range(len(pizza[0]))] for _ in pizza] # the number of apples directly down, not including it

        for row in range(len(pizza)-1, -1, -1):
            for col in range(len(pizza[0])-1, -1, -1):
                
                if col != len(pizza[0]) -1:
                    num_right[row][col] += num_right[row][col+1] + grid[row][col+1]
                if row != len(pizza) - 1:
                    num_lower[row][col] += num_lower[row+1][col] + grid[row+1][col]
        # right -> left -> start at right at row above
        for row in range(len(pizza)-1, -1, -1):
            for col in range(len(pizza[0])-1, -1, -1):
                num_lower_right[row][col] += grid[row][col] + num_right[row][col] + num_lower[row][col]
                
                if col != len(pizza[0]) -1 and row != len(pizza) -1:
                    num_lower_right[row][col] += num_lower_right[row+1][col+1]

        


        @lru_cache(None)
        def solve(row, col, cur_k):
            
            if row >= len(pizza) or col >= len(pizza[0]):
                return 0
            if cur_k == 0 and num_lower_right[row][col] > 0:
                return 1
            if num_lower_right[row][col] == 0:
                return 0
            out = 0
            for horizontal_split in range(row, len(pizza)-1):
                if num_lower_right[row][col] - num_lower_right[horizontal_split+1][col] > 0:
                    out += solve(horizontal_split+1, col, cur_k-1)
            for v in range(col, len(pizza[0]) -1):
                if num_lower_right[row][col] - num_lower_right[row][v+1] > 0:
                    out += solve(row, v+1, cur_k-1)

            return out

        return solve(0, 0, k-1) % (10**9+7)
