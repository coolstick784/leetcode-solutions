class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        # Have a list of cells that we've already explored in a set
        # From each water block, set the current distance to 0
        # Add each block to what we've already explored
        # Go further with each one to the left, right, up, and down
        explored = set()
        prev = set()
        for r, row in enumerate(grid):
            for c, el in enumerate(row):
                if el == 1:
                    prev.add((r, c))

        cur_dist = -1
        add_dist = 1
        while add_dist:
            to_add = set()
            add_dist = 0
            for r, c in prev:
                if (r, c) not in explored and r < len(grid) and c < len(grid[0]) and r >= 0 and c >= 0:
                    add_dist = 1
                    explored.add((r, c))
                    to_add.add((r+1, c))
                    to_add.add((r-1, c))
                    to_add.add((r, c+1))
                    to_add.add((r, c-1))


        
            prev = to_add
            cur_dist += add_dist
        if cur_dist == 0:
            return -1
        return cur_dist

