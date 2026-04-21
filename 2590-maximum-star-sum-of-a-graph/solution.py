# define the conns for each edge, then sum up all of them that are > 0 + the val itself?

class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        res = float("-inf")
        edges_dict = {}
        for n in range(len(vals)):
            edges_dict[n] = []
        for start, end in edges:
            edges_dict[start].append(vals[end])
            edges_dict[end].append(vals[start])
        for edge in edges_dict:
            edges_dict[edge].sort()
            edges_dict[edge].reverse()
        
        for edge in edges_dict:
            res = max(res, vals[edge] + sum([v for v in edges_dict[edge][:k] if v > 0]))
        return res
