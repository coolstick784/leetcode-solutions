class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        i = 0
        j = 0
        explored = set()
        def explore(i, j, prev, dn):

            
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0:
                return False

            val = grid[i][j]
            if (val != 3 and val != 5) and dn == "r" and val != 1:
                return False
            if dn == "l" and val != 4 and val != 6 and val != 1:
                return False
            if dn == "u" and val != 4 and val != 3 and val != 2:
                return False
            if dn == "d" and val != 5 and val != 6 and val != 2:
                return False
            if i == len(grid) -1 and j == len(grid[0]) -1:
                return True
            if (i, j) in explored:
                return False

            explored.add((i, j))
            if val == 1:
                return explore(i, j+1, val,"r") or explore(i, j-1, val,"l")
            if val == 2:
                return explore(i+1, j, val,"d") or explore(i-1, j, val,"u")
            if val == 3:
                return explore(i+1, j, val,"d") or explore(i, j-1, val,"l")
            if val == 4:
                return explore(i+1, j, val,"d") or explore(i,j+1,val, "r")
            if val == 5:
                return explore(i, j-1, val, "l") or explore(i-1, j, val, "u")
            if val == 6:
                return explore(i-1, j, val, "u") or explore(i, j+1, val, "r")
            
        return explore(0, 0, 0, "")
