class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        heap = []
        paths = {}
        for start, end, cost in edges:
            paths.setdefault(start, []).append((cost, end, 0))
            paths.setdefault(end, []).append((cost*2, start, 1))
        
        cur = 0
        costs = {0:0}
        cur_el = (0, 0, 0)
        heapq.heappush(heap, cur_el)
        while heap:
            cur_el = heapq.heappop(heap)
            if costs[cur_el[1]] != cur_el[0]:
                continue
            if cur_el[1] == n - 1:
                return cur_el[0]
            for path in paths.get(cur_el[1], []):
                poss_cost = path[0] + cur_el[0]

                if poss_cost < costs.get(path[1], float('inf')):
                    heapq.heappush(heap, (poss_cost, path[1], path[2] + cur_el[2]))
                    costs[path[1]] = poss_cost
                
        return -1
            
                
        
        
