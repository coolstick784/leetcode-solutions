import heapq
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        starts = {}
        ends = {}
        for start, end in relations:
            starts.setdefault(start, set()).add(end)
            ends.setdefault(end, set()).add(start)
        heap = []
        best = {}
        
        for i in range(1,n+1):
            if i not in ends:
                heapq.heappush(heap, (time[i-1], i))
                best[i] = time[i-1]
        while heap:
            t, cur = heapq.heappop(heap)
            for end in starts.get(cur, set()):
                ends[end].remove(cur)
                if not ends[end]:
                    new = t + time[end-1]
                    if new < best.get(end, float('inf')):
                        heapq.heappush(heap, (new, end))
                        best[end] = new


        return max(best.values())
