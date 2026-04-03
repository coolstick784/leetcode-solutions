# we want 2 dictionaries
# 1 is a grid, that holds a grid number as the key and all station numbers in a list
# 2 is a station index, that holds the index as the key and the grid number as the value
# sort each grid dictionary value
# when we remove a grid, just remove it from that grid's list
# we can use breadth first search to add elements to a grid
# we want a connections dict, where for each input we have a list of outputs
# first, we'll want to ensure there are no duplicate connections by adding their sorted tuples to a set
# then, we'll have an input and output for each connection
# we'll want a list of stations we've already explored
# for each input, we'll add the list of outputs to that grid
# for each output, we'll then see if it's in explored
# if it is, we'll do nothing
# if it isn't, add each of those outputs to said grid
class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:

        explored = set()
        conns_dict = {}
        station_dict = {}
        grid_num = 1
        grid_dict = {}
        for inp, out in connections:
            conns_dict.setdefault(inp, []).append(out)
            conns_dict.setdefault(out, []).append(inp)

        def add_grid(cur, grid_num):
            if cur in explored:
                return 
            grid_dict[grid_num].append(cur)
            station_dict[cur] = grid_num
            explored.add(cur)
            if cur not in conns_dict:
                return
            for next_out in conns_dict[cur]:
                add_grid(next_out, grid_num)
 
        for inp in conns_dict:
            if inp in explored:
                continue
            explored.add(inp)
            grid_dict.setdefault(grid_num, []).append(inp)
            station_dict[inp] = grid_num
            out = conns_dict[inp]
            for cur in out:
                add_grid(cur, grid_num)
            grid_num += 1

        for num in range(1, c+1):
            if num not in explored:
                explored.add(num)
                grid_dict[grid_num] =[num]
                station_dict[num] = grid_num
                grid_num += 1
        
        sorted_grids = {} # this will be a tuple, with [0] being the list and [1] being the index of the min
        for grid in grid_dict:
            grid_dict[grid].sort()
            sorted_grids[grid] = [grid_dict[grid], 0]
            grid_dict[grid] = set(grid_dict[grid])



        res = []
        for t, num in queries:
            cur_grid_num = station_dict[num]
            cur_grid = grid_dict[cur_grid_num]
            if t == 1:
            
                if cur_grid == set():
                    res.append(-1)
                elif num in cur_grid:

                    res.append(num)
                else:
              
                    
                    min_idx = sorted_grids[cur_grid_num][1]
                    res.append(sorted_grids[cur_grid_num][0][min_idx])
            else:

                if num in cur_grid:

                    cur_grid.remove(num)
                    min_idx = sorted_grids[cur_grid_num][1]
                    cur_val = sorted_grids[cur_grid_num][0][min_idx]
                    while cur_val not in cur_grid and min_idx < len(sorted_grids[cur_grid_num][0])-1:
                        min_idx += 1
                        cur_val = sorted_grids[cur_grid_num][0][min_idx]
                    sorted_grids[cur_grid_num][1] = min_idx
                    


        return res
        
