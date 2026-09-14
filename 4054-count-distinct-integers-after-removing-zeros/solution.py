from collections import deque
class Solution:
    def countDistinct(self, n: int) -> int:
        
        if n < 10:
            return n
        
        pows = [1]
        while len(pows) < 20:
            pows.append(10*pows[-1])
        

        @lru_cache(None)
        def solve(l):
            
            if l == 0:
                return 0
            return 9 ** l + solve(l-1)
        lower = len(str(pows[bisect.bisect(pows, n) - 1]))-1
        res = solve(lower)

        cur = len(str(n))
        q = deque(str(n))
        l = len(q)
        broke = False
        while q:
            num = int(q.popleft())
            if num == 0:
                broke = True
                break
            l -= 1
            res += max(num-1, 0) * max(9**l, 1)
            
            prev = num
        if not broke:
            res += 1
        
        return res 
            
