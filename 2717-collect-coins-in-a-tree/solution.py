# get all the edges that are only connected to one element
# if that edge has a coin, combine it with the one it connects to and say it has a max dist of 1
# otherwise, just move to the one it connects to 
# if a coin has a max dist of 2, we can't increase it
# so we can't expand from there, but we can expand from the other side
# and we subtract 1 from n every time we remove a coin

from collections import deque
class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        if not edges:
            return 0

        n = len(coins)
        conns = {}
        for start, end in edges:
            conns.setdefault(start, set()).add(end)
            conns.setdefault(end, set()).add(start)
        q= deque()
        in_q = set()
        for c in conns:
            if len(conns[c]) == 1:
                q.append(c)
                in_q.add(c)
        maxDist = {}
        removed = set()
        while q:
            cur =  q.popleft()
            dist = maxDist.get(cur, 0)
            
            if dist >= 2:
                continue
            if len(conns[cur]) == 0 and coins[cur]:
                continue
            elif len(conns[cur]) == 0 and not coins[cur]:
                removed.add(cur)
                n -= 1
                continue
            removed.add(cur)
            
            n -= 1
            conn = next(iter(conns[cur]))
            conns[cur].remove(conn)
            conns[conn].remove(cur)
            if coins[cur]:
                maxDist[conn] = max(maxDist.get(conn, 0), maxDist.get(cur, 0) + 1)
                coins[conn] += 1
            if maxDist.get(conn, 0) < 2 and len(conns[conn]) == 1:
                q.append(conn)
        
                
        
        return max(0, (n-1) * 2)
