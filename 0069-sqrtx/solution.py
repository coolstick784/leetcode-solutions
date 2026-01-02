class Solution:
    def mySqrt(self, x: int) -> int:
        
        for y in range(x+2):
            if y * y > x:
                return y-1 

        
