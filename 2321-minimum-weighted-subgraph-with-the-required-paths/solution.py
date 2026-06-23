# we want to know 3 things:
# 1. the cost from src1 to node n
# 2. the cost from src2 to node n
# 3. the cost from n to dest
# minimize the summed cost of these three

class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        s1 = [float('inf') for _ in range(n)]
        s2 = [float('inf') for _ in range(n)]
        dst = [float('inf') for _ in range(n)]
        s1[src1] = 0
        s2[src2] = 0
        dst[dest] = 0
        conns = {}
        rev = {}
        for start, end, w in edges:
            conns.setdefault(start, set()).add((end, w))
            rev.setdefault(end, set()).add((start, w))
     
        
        def explore(cur, node, option):
            if option == "s1":
                l = s1
            elif option == "s2":
                l = s2
            else:
                l = dst
            if cur >= l[node]:
                return
            l[node] = cur
            heapq.heappush(heap, (cur, node))
        
        heap = [(0, src1)]
        while heap:
            cost, node = heapq.heappop(heap)
            for conn, w in conns.get(node, set()):
                explore(cost+w, conn, "s1")
        heap = [(0, src2)]
        while heap:
            cost, node = heapq.heappop(heap)
            for conn, w in conns.get(node, set()):
                
                explore(cost+w, conn, "s2")
        heap = [(0, dest)]
        while heap:
            cost, node = heapq.heappop(heap)
            for conn, w in rev.get(node, set()):
                explore(cost+w, conn, "dst")



        out = [s1[i] + s2[i] + dst[i] for i in range(n)]
        return min(out) if min(out) < float('inf') else -1
