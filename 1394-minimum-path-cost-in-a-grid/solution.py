class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        cur = {}
        for c, el in enumerate(grid[0]):
            cur[el] = el
        print("cur", cur)
        for r, row in enumerate(grid[1:]):
            new = {}
            for c, el in enumerate(row):
                for val in cur:
                    cost = cur[val]
                    new_cost = moveCost[val][c]
                    
                    new[el] = min(new.get(el, float('inf')), cost + new_cost + el)
                   

            cur = new.copy()
        
        return min(cur.values())
