# always go for the option that has the least distance from the solution

from collections import deque
class Solution:
    def minimumFlips(self, n: int, edges: List[List[int]], start: str, target: str) -> List[int]:
        conns = {}
        conns[0] = set()
        for idx, (s, e) in enumerate(edges):
            conns.setdefault(s, set()).add((idx, e))
            conns.setdefault(e, set()).add((idx, s))

        res = set()
        q = deque()
        needs_change = {}
        for i in range(n):
            if len(conns[i]) == 1:
                q.append(i)
            if start[i] != target[i]:
                needs_change[i] = True
            else:
                needs_change[i] = False
    
        while q:
            i = q.popleft()
  

            if len(conns[i]) == 0:
                if needs_change[i]:
                    return [-1]
                continue
            idx, c = next(iter(conns[i]))
            

            conns[i].remove((idx, c))
            conns[c].remove((idx, i))
            if needs_change[i]:
                needs_change[c] = not needs_change[c]
                res.add(idx)
            
            if len(conns[c]) == 1:
                q.append(c)


        out = []
        for idx in range(n):
            if idx in res:
                out.append(idx)
        return out
