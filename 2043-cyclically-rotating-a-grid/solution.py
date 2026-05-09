# loop through the grid once, and assign each index to a group, top left should be #1 and so on, so each group should have a list in a dict
# then, simply add the cycles and loop through each element
# we can have an explored set, where we start at the top left, and we go down one cell while we can't anymore, then we go right, then up, then left until we reach our top left
# then add 1 to the row and one to the col

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        self.groups = {}
        explored = set()
        self.cur_group = 1
        def isValid(coords):
            x, y = coords
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or coords in explored:
                return False
            return True
        def explore(cur, dn):
            x, y = cur
            explored.add(cur)
            self.groups.setdefault(self.cur_group, []).append(cur)

            if dn == "down":
                if isValid((x+1, y)):
                    explore((x+1, y), "down")
                    return 
                elif isValid((x, y+1)):
                    explore((x, y+1), "right")
                    return 
            elif dn == "right":
                if isValid((x, y+1)):
                    explore((x, y+1), "right")
                    return 
                elif isValid((x-1, y)):
                    explore((x-1, y), "up")
                    return
            elif dn == "up":
                if isValid((x-1, y)):
                    explore((x-1, y), "up")
                    return
                elif isValid((x, y-1)):
                    explore((x, y-1), "left")
                    return
            else:
                if isValid((x, y-1)):
                    explore((x, y-1), "left")
                    return

            if isValid((x+1, y)):
                self.cur_group += 1
                explore((x+1, y), "down")
        
             
        explore((0, 0), "down")
        res = [[None for _ in grid[0]] for _ in grid]

        for coords in self.groups.values():
            n = len(coords)
            for idx, c in enumerate(coords):
                px, py = c
                new_coord = coords[(idx + k) % n]
                x, y = new_coord

                res[x][y] = grid[px][py]


        return res
