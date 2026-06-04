from collections import deque
class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        
        def findMinPath(edges):
            if not edges:
                return 1
            cur = {}
            mn = {}
            res = float('inf')
            for start, end in edges:
                cur.setdefault(start, set()).add(end)
                cur.setdefault(end, set()).add(start)
                mn[start] = 1
                mn[end] = 1
            q = deque()
            for start in cur:
                if len(cur[start]) == 1:
                    q.append(start)
            while q:
                start = q.popleft()
   
                val = mn[start] 
                end = next(iter(cur[start]))
                cur[start].remove(end)
                cur[end].remove(start)
                mn[end] = max(1 + mn[start], mn[end])

                if len(cur[end]) == 0:
                    
                    return mn[end]
                if len(cur[end]) == 1:
                    q.append(end)
            
        def findMaxPath(edges):
            if not edges:
                return 1
            cur = {}
            mn = {}
            mx = {}
            res = float('inf')
            for start, end in edges:
                cur.setdefault(start, set()).add(end)
                cur.setdefault(end, set()).add(start)
                mn[start] = 1
                mn[end] = 1
                mx[start] = [0, 0]
                mx[end] = [0, 0 ]
            q = deque()
            for start in cur:
                if len(cur[start]) == 1:
                    q.append(start)
            while q:
                start = q.popleft()
   
                val = mn[start] 
                end = next(iter(cur[start]))
                cur[start].remove(end)
                cur[end].remove(start)
                heapq.heappush(mx[end], max(mx[start][0] + 1, mx[start][1]+1))
                while len(mx[end]) > 2:
                    heapq.heappop(mx[end])

                if len(cur[end]) == 0:
          
                    return mx[end][0] + mx[end][1] 
                if len(cur[end]) == 1:
                    q.append(end)


        return max(findMinPath(edges1) + findMinPath(edges2) -1, findMaxPath(edges1), findMaxPath(edges2))
