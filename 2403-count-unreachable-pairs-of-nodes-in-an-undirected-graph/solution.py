class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        union = [i for i in range(n)]
        conns = {}
        def trace(cur):
            if union[cur] == cur:
                return cur
            val = trace(union[cur])
            union[cur] = val
            return val
        def join(start, end):
            union[trace(union[end])] = trace(union[start])
            return 
        for start, end in edges:
            join(start, end)

        ctr = Counter([trace(i) for i in range(n)])
        res = 0
        
        for i in ctr:
            res += ctr[i] * (n - ctr[i])
            n -= ctr[i]

        return res
