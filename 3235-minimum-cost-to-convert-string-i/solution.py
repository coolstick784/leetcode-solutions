from typing import List
import heapq

class Solution:
    def minimumCost(self, source: str, target: str,
                    original: List[str], changed: List[str], cost: List[int]) -> int:

        # Build min direct edge cost for each pair
        costs = {}
        for i, a in enumerate(original):
            b = changed[i]
            key = a + b
            if key not in costs:
                costs[key] = cost[i]
            else:
                costs[key] = min(costs[key], cost[i])

        # Build adjacency list once (forward edges)
        graph = {}
        for key, w in costs.items():
            a, b = key[0], key[1]
            graph.setdefault(a, []).append((b, w))

        solves = {}

        # Replace recursion+trail with shortest path (Dijkstra) on letters
        def solve(char: str, goal: str) -> int:
            if char == goal:
                return 0

            # Dijkstra from char to goal
            dist = {char: 0}
            heap = [(0, char)]
            while heap:
                d, u = heapq.heappop(heap)
                if d != dist.get(u):
                    continue
                if u == goal:
                    return d
                for v, w in graph.get(u, []):
                    nd = d + w
                    if nd < dist.get(v, float('inf')):
                        dist[v] = nd
                        heapq.heappush(heap, (nd, v))
            return float('inf')

        res = 0
        for i, s_ch in enumerate(source):
            key = s_ch + target[i]
            if key not in solves:
                solves[key] = solve(s_ch, target[i])

            cur = solves[key]
            if cur == float('inf'):
                return -1
            res += cur

        return res

