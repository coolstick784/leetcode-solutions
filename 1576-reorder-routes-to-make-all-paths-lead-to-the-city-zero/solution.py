class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # If a city is going away from 0, make it go toward 0
        # If a city is going toward 0, keep it
        
        
        # Define the destination for each city in a dictionary, where the key is the destination and each key has a list that ends in that key
        
        # For each destination, if it's not in a direct path to 0, add 1 to the total, add it to our direct path list, and continue
        
        paths_end = {}
        paths_start = {}
        direct_paths = set([0])
        for origin, destination in connections:
            paths_end[destination] = paths_end.get(destination, []) + [origin]
            paths_start[origin] = paths_start.get(origin, []) + [destination]
        res = 0
        
        q = deque([0])
        while q:
            explore_next = q.popleft()

            for p in paths_end.get(explore_next, []):
                q.append(p)
                direct_paths.add(p)
            for p in paths_start.get(explore_next, []):
                if p not in direct_paths:
                    q.append(p)
                    
                    direct_paths.add(p)
                    res += 1

        return res
                    
            
        
        
            
            
        
