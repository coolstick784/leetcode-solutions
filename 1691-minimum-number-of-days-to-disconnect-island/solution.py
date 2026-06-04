# the max # is 2
# for each land cell, check if it has one on top, right, left, bottom
 
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:

        def noConns(r1=None, c1=None, r2=None, c2=None):
            unions = {}
            def trace(cur):
                if unions[cur] == cur:
                    return cur
                val = trace(unions[cur])
                unions[cur] = val
                return val
            def union(src, target):
                tsrc = trace(src)
                tgt = trace(target)
                if tsrc != tgt:
                    unions[tgt] = trace(src)

            for r, row in enumerate(grid):
                for c, el in enumerate(row):
                    if (r == r1 and c == c1) or (r == r2 and c == c2) or el == 0:
                        continue
                    unions[(r, c)] = (r, c)
                    if unions.get((r-1, c)):
                        union((r, c), (r-1, c))
                    if unions.get((r, c-1)):
                        union((r, c), (r, c-1))
                    
                    
            n = 0 
            for v in unions:
                if unions[v] == v:
                    n += 1
            return n != 1 



        if noConns():
            return 0
        els = []
        for r, row in enumerate(grid):
            for c, el in enumerate(row):
                if el:
                    els.append((r, c))

        for r, c in els:
            if noConns(r, c):
                return 1
        return 2


        

