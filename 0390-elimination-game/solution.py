# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [2, 4, 6, 8]
# [2, 6]
# [2]

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [2, 4, 6, 8, 10]
# [4, 8]
# 8
class Solution:
    def lastRemaining(self, n: int) -> int:
   
        def solve(cur, start):
         
            if cur == 1:
    
                return 1
            if start:
          
                return solve(cur//2, False) * 2
            if not start and cur % 2 == 1:
                return solve(cur//2, True) * 2
            if not start and cur % 2 == 0:
                

                return solve(cur//2, True) *2 - 1

        return solve(n, True)
            
            
