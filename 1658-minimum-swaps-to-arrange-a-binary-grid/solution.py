class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        # Find the closest one at row n, with len(grid) -1-n zeros to the left
        # Swap them, and then find the next closest, and keep going


        
        zeros_grid = []
        for idx, r in enumerate(grid):

            cur = 0
            for right, c in enumerate(r[::-1]):
                if c == 0:
                    cur += 1
                else:
                    break
            zeros_grid.append(cur)
        
        res = 0
  
        new_grid = zeros_grid.copy()
        for idx, r in enumerate(zeros_grid):
            goal_n = len(grid) - idx - 1


            for idx2, r2 in enumerate(zeros_grid[idx:]):

                if r2 >= goal_n:

                    res += idx2
                    new_grid[idx], new_grid[idx2+idx] = new_grid[idx2+idx], new_grid[idx]
                    break
                else:
                    new_grid[idx], new_grid[idx2+idx] = new_grid[idx2+idx], new_grid[idx]
                if r2 < goal_n and idx2+idx == len(grid) - 1:
                    return -1
            zeros_grid = new_grid.copy()
     



        return res

        

            



        
