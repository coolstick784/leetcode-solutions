# for each cell, we want to know if a guard can see them from the left, right, up, or down
# if the left cell can't be seen, then we can't be seen from the left
# if a guard is in that cell, that cell can be seen 
# if a wall is in that cell, that cell can't be seen

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        can_be_seen = [[[False, False, False, False] for _ in range(n)] for _ in range(m)] #left, right, up, down

        guards_set = set()
        walls_set = set()
        for x, y in guards:
            guards_set.add((x, y))
        for x, y in walls:
            walls_set.add((x, y))
        for row in range(m):
            for col in range(n):
                if (row, col) in guards_set:
                    can_be_seen[row][col] = [True, True, True, True]
                elif (row, col) in walls_set:
                    can_be_seen[row][col] = [False, False, False, False]
                else:
                    if row > 0 and can_be_seen[row-1][col][2] == True:
                        can_be_seen[row][col][2] = True
                    if col > 0 and can_be_seen[row][col-1][0] == True:
                        can_be_seen[row][col][0] = True
        for row in range(m-1, -1, -1):
            for col in range(n-1, -1, -1):
                if (row, col) in guards_set:
                    can_be_seen[row][col] = [True, True, True, True]
                elif (row, col) in walls_set:
                    can_be_seen[row][col] = [False, False, False, False]
                else:
                    if row < (m-1) and can_be_seen[row+1][col][3] == True:
                        can_be_seen[row][col][3] = True
                    if col < (n-1) and can_be_seen[row][col+1][1] == True:
                        can_be_seen[row][col][1] = True
        res = 0
        for row in range(m):
            for col in range(n):
                if sum(can_be_seen[row][col]) == 0 and (row, col) not in guards_set and (row, col) not in walls_set:
                    res += 1
        return res
