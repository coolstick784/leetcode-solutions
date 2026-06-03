# look at the nodes with only 1 edge and ask if they can be disconnected
# if so, add 1 to res
# otherwise, add their score to their connection's score

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        num_edges = {}
        all_edges = {}
        if not edges:
            return 1
        for start, end in edges:
            all_edges.setdefault(start, set()).add(end)
            all_edges.setdefault(end, set()).add(start)
        for e in all_edges:
            num_edges.setdefault(len(all_edges[e]), []).append(e)
        res = 0
        while num_edges.get(1, []):
            e = num_edges[1].pop()

            if values[e] % k == 0:
                res += 1
              
            if all_edges[e]:
                end = list(all_edges[e])[0]
                values[end] += values[e]
                
                l = len(all_edges[end])
                all_edges[end].remove(e)


                num_edges.setdefault(l-1, []).append(end)


        
        return res
