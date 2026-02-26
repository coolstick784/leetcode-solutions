class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        
        for n in range(1, numRows+1):
            if n == 1:
                res.append([1])
            else:
 
                out = []
                prev = res[-1]
                for idx, n in enumerate(prev):
                    if idx == 0 :
                        out.append(1)
                    else:
                        out.append(n + prev[idx-1])
                out.append(1)
                        
                
                res.append(out)
        return res
        
