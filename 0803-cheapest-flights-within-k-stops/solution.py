class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        mp = {}
        for f, t, p in flights:
            mp.setdefault(f, []).append((t, p))
        best = {}
        
        best.setdefault(src, {})[0] = 0

        heap = [(0, 0, src)] # price, # trips, spot

        def solve(dest, n, p):
            if n > k+1:
                return 
            cur_best = best.get(dest, {}).get(n, float('inf'))
            if p < cur_best:
                best.setdefault(dest, {})[n] = p
                heapq.heappush(heap, (p, n, dest))

     
        while heap:
     
            p, n, s = heapq.heappop(heap)
            if s == dst:
                return p
            for d, add in mp.get(s, []):
               
                solve(d, n+1, p + add)
        return -1

