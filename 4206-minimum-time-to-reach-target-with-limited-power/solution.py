import heapq
class Solution:
    def minTimeMaxPower(self, n: int, edges: List[List[int]], power: int, cost: List[int], source: int, target: int) -> List[int]:
        answer = [float('inf'), -float('inf')]
        conns = {}
        for start, end, t in edges:
            conns.setdefault(start, set()).add((end, t))

        @lru_cache(None)
        def best_time(node, start):
            if node == target:
                return [0, start]
            cur = start - cost[node]
            if cur < 0:
                return [float('inf'), -float('inf')]
            out = float('inf')
            max_p = -float('inf')
            for end, t in conns.get(node, set()):
                
                new_t, new_p = best_time(end, cur)
                cur_t = t + new_t
                if cur_t < out:
                    out = cur_t
                    max_p = new_p
                elif cur_t == out:
                    max_p = max(max_p, new_p)
                

            return (out, max_p)

        
        answer = list(best_time(source, power))
        if answer[0] == float('inf'):
            return [-1, -1]


        return answer
