class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # We have the time it takes to get to each node
        # Go to a node, then gather the possible nodes it can go to
        # If the time it would take to get to that node is < the minimum time, update the minimum time and go to that node
        # We want a dictionary so that when we get to a node, we know each node it goes to, as well as the time it takes to go to each node
        
        times_dict = {}
        for source, target, time in times:
            
            times_dict.setdefault(source, []).append((target, time))
        
        heap = []
        min_times = [2**31-1 for _ in range(n)] # Node 1 corresponds to index 0, node 2 index 1, etc
        heapq.heappush(heap, (k, 0))

        while heap:

            cur = heapq.heappop(heap)
            n = cur[0]
            t = cur[1]
            if t < min_times[n-1]:
                min_times[n-1] = t
                for node, time in times_dict.get(n, []):
                    heapq.heappush(heap, (node, time+t))
                
            
        max_time = max(min_times)
        if max_time == 2**31-1:
            return -1
        return max_time
