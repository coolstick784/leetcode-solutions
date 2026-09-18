
class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        vals = [1]
        if k == 1:
            return 1
        for n in range(2, k+1):
            vals.append((vals[-1] * 10 + 1) % k)
            
            if vals[-1] == 0:
                return n
  
  
        return -1
