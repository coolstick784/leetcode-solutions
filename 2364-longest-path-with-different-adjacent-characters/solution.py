# start with the ones that have no children
# each node can have two directions it goes 
# for the ones with no children, however, it can only go one direction
# so if each node is included, it's the sum of the two highest directions it can go

from collections import deque
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        best = {} # for each index, it will have the two highest directions
        children = {}
        q = deque()
        res = 1
        for idx, p in enumerate(parent):

            children.setdefault(p, set()).add(idx)
        for idx in range(len(parent)):
            if idx not in children:
                q.append(idx)
        while q:
            node = q.popleft()
            best.setdefault(node, [0])
            p = parent[node]
            best.setdefault(p, [0])
            best[node] = sorted(best[node])
            best[node].reverse()
            best[node] = best[node][:2]
            score = sum(best[node]) + 1

            res = max(res, score)
            
            children[p].remove(node)
            if s[node] != s[p]:
                best[p].append(best[node][0] + 1)
            if not children[p] and p != -1:
                q.append(p)
        return res



