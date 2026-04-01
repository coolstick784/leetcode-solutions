class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        G = [{} for i in range(n)]
        for i,j,w in edges:
            G[j][i] = min(G[j].get(i, inf), w)
        h = [[0, 0]]
        seen = [inf] * n
        k = n
        while h and k > 0:
            d, i = heappop(h)
            if seen[i] < inf: continue
            k -= 1
            seen[i] = d
            for j in G[i]:
                if seen[j] < inf: continue
                heappush(h, [G[i][j], j])
        return -1 if k > 0 else max(seen)
