class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        heap = []
        conns = {}
        for start, end, time in edges:
            conns.setdefault(start, set()).add((end, time))
            conns.setdefault(end, set()).add((start, time))
        heap = [(0, 0)]
        best = {}
        best[0] = 0
        while heap:
            
            time, cur = heapq.heappop(heap)
            if time >= disappear[cur]:
                if cur in conns:
                    del conns[cur]
                continue
            
            for end, t in conns.get(cur, set()):
                
                newTime = time + t
                if end not in conns:
                    continue
                
                if newTime < best.get(end, float('inf')) and newTime < disappear[end]:
 
                    heapq.heappush(heap, (newTime, end))
                    best[end] = newTime
            if cur in conns:
                del conns[cur]

                
        
        res = [-1 for _ in range(n)]
        for i in range(n):
            res[i] = best.get(i, -1)
        return res
