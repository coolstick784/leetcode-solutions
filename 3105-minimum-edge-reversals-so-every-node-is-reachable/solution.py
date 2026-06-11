from collections import deque
class Node:
    def __init__(self, val, left=None, right=None, parent=None):
        self.left = left
        self.val = val
        self.right = right
        self.parent = parent
class Solution:

    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        paths = {}
        conns = {}
        for start, end in edges:
            paths.setdefault(start, set()).add(end)
            conns.setdefault(end,set()).add(start)
            conns.setdefault(start, set()).add(end)
        explored = set()
        tmp = conns.copy()
        
        res = {} # base, conns
        q = deque()
        descendants = {}
        self.start = None
        def explore(i):
            if len(tmp[i]) == 0:
                self.start = i
                return 
            end = next(iter(tmp[i]))
            tmp[i].remove(end)
            tmp[end].remove(i)
            # res.setdefault(end, {})
            # res.setdefault(i, {})
            # if end in paths.get(i, []):
            #     res[i]['base'] = 0 + res[i].get('base', 0)
            #     res[end]['base'] = 1 + res[end].get('base', 0)

            # else:
            #     res[i]['base'] = 1 + res[i].get('base', 0)
            #     res[end]['base'] = 0 + res[end].get('base', 0)
            descendants.setdefault(end, set()).add(i)
            if len(tmp[end]) == 1:
                q.append(end)


        def solve(i):
            
            res.setdefault(i, 0)
            for d in descendants.get(i, set()):
                
                res[i] += solve(d)
                if d not in paths.get(i, []):
                    res[i] += 1
            return res[i]
        


        def bfs(i):
            for d in descendants.get(i, set()):
                res[d] = res[i]
                if d not in paths.get(i, set()):
                    res[d] -= 1
                else:
                    res[d] += 1
                bfs(d)

        
        for i in range(n):
            if len(conns[i])== 1:
                q.append(i)

        while q:
            explore(q.popleft())
        
        solve(self.start)
        bfs(self.start)
        
        out = []
        for i in range(n):
            out.append(res[i])
        return out
