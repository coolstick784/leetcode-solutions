class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        explored = set()
        
        res = 0
        def search(r, c):

            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                return False
            if grid[r][c] == 1:
                return True
            if (r, c) in cur_explored:
                return True
            explored.add((r, c))
            cur_explored.add((r, c))
            
        
            return search(r+1, c) and search(r-1, c) and search(r, c+1) and search(r, c-1)
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                el = grid[r][c]
                if el == 1:
                    continue
                if (r, c) not in explored:
                    cur_explored = set()
                    if search(r, c):
                        res += 1
        return res
