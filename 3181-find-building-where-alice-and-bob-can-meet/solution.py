from collections import deque
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        mp = {}
        res = [-1 for _ in queries]
        for idx, (start, end) in enumerate(queries):
            if start > end:
                start, end = end, start
                queries[idx] = [start, end]
            mp.setdefault((start, end), []).append(idx)
        qs = deque(sorted([(end, start) for start, end in queries]))
        
        heap = []
        for idx, h in enumerate(heights):
            while qs and qs[0][0] <= idx:
                end, start = qs.popleft()
                if heights[end] > heights[start] or start == end:
                    res[mp[(start, end)].pop()] = end
                    continue
                heapq.heappush(heap, (heights[start], start, end))
            while heap and h > heap[0][0]:
                _, start, end = heapq.heappop(heap)
                res[mp[(start,end)].pop()] = idx
        return res

