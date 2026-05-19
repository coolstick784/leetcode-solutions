# dict with the top left

# loop through each row/col in g1
# do dfs to explore each row/col individually
# if it's already explored, dont do anything
# otherwise, if it's land, add that to an island with that idx
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:



        def explore(grid):
            explored = set()
            out_dict = {}

            def dfs(r, c, prev):
                if (r, c) in explored or r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                    return
                explored.add((r, c))
                if grid[r][c] == 1:
                    out_dict[prev].add((r, c))
                    dfs(r+1, c, prev)
                    dfs(r-1, c, prev)
                    dfs(r, c+1, prev)
                    dfs(r, c-1, prev)
            for r, row in enumerate(grid):
                for c, el in enumerate(row):
                    if (r, c) in explored:
                        continue
                    explored.add((r, c))
                    if el == 1:
                        out_dict[(r, c)] = set({(r, c)})
                        dfs(r+1, c, (r, c))
                        dfs(r-1, c, (r, c))
                        dfs(r, c+1, (r, c))
                        dfs(r, c-1, (r, c))
            return out_dict


    
        g2_islands = explore(grid2)

        res = 0
        for island in g2_islands.values():
            good = True
            for r, c in island:
                if grid1[r][c] == 0:
                    good = False
                    break

            if good:
                res += 1

        return res
