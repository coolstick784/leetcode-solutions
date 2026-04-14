class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        res = {0:1}
        starts = {}
        for start, end, units in conversions:
            starts.setdefault(start, []).append((end, units))
        def bfs(start):
            cur = starts.get(start, None)
            if not cur:
                return
            cur_res = res[start]
            for end, units in cur:
                res[end] = cur_res * units % (10**9+7)
                bfs(end)


        bfs(0)

        

        out = [1]
        for n in range(len(conversions)):
            out.append(res[n+1] )
        return out
            
        
