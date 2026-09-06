class Solution:
    def splitString(self, s: str) -> bool:
        @lru_cache(None)
        def solve(idx, cur_start = 0, prev = None):
            #print(idx, cur_start, prev)
            if idx == len(s) - 1 and cur_start == 0:
                return False 
            if idx >= len(s):
                return False
            cur_s = s[cur_start:idx+1]
            cur_n = int(cur_s)
            if prev is None:
                if solve(idx+1, idx+1, cur_n):
                    return True
                if solve(idx+1, 0, None):
                    return True
                return False
            if cur_n == prev - 1:
                print("idx is less than", idx)
                if idx == len(s) - 1:
                    return True
                if solve(idx+1, idx+1, cur_n):
                    return True
            if solve(idx+1, cur_start, prev):
                return True
            return False
            
             

        return solve(0, 0)
