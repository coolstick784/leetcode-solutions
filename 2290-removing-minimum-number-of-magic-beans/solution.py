class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        cost = sum(beans)
        num_left = len(beans)
        ctr = Counter(beans)
        beans = [(n, ct) for n, ct in ctr.items()]
        beans.sort()
        
        res = cost
        cur = 0
        s = 0
        
        for n, ct in beans:
            diff = n - cur
           
            cost -= (diff * num_left)
            num_left -= ct
            
            cur = n
            
            res = min(res, s + cost)
            #print("N", n, "ct", ct, "res", res, "s", s, "cost", cost)
            s += n * ct
        return res
        
