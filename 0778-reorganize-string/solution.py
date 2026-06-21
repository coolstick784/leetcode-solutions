from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        ctr = Counter(s)
        heap = []
        for ch in ctr:
            heapq.heappush(heap, (-ctr[ch], ch))
        prev = None
        res = []
        while heap:

            ct, ch = heapq.heappop(heap)
            
            
            ct = -ct
            if ch == prev:
                if not heap:
                    return ""
                n_ct, n_ch = heapq.heappop(heap)
                n_ct = -n_ct
                heapq.heappush(heap, (-ct, ch))
                if n_ct > 1:
                    
                    heapq.heappush(heap, (-(n_ct-1), n_ch))
                res.append(n_ch)
                prev = n_ch
            else:
                if ct > 1:
                    heapq.heappush(heap, (-ct+1, ch))
                res.append(ch)
                prev = ch
        return "".join(res)
