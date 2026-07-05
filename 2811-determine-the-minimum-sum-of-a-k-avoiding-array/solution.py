class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        
        s =  0
        poss = set([i for i in range(1, n+k+1)])
        res = []
        for i in range(1, n+k+1):
            if i not in poss:
                continue
            res.append(i)
            s += i
            
            if k - i in poss:
                poss.remove(k-i)
            if len(res) == n:
      
                return s


