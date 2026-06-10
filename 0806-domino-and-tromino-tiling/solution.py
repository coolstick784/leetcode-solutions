class Solution:
    def numTilings(self, n: int) -> int:
        @lru_cache(None)
        def endTop(cur):
         
            
            if cur <= 0:
                return 0
            if cur == 1:
                return 0
            if cur == 2:
                return 1
            return (end(cur-2) + endTop(cur-1)) % (10**9+7)
        @lru_cache(None)
        def end(cur):
  
            if cur <= 0:
                return 0
            if cur == 1:
                return 1
            if cur == 2:
                return 2
            return (endTop(cur-1) * 2 + end(cur-1) + end(cur-2)) % (10**9+7)
        
        return end(n)
