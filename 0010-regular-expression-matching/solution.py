class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        letters = set([chr(ord('a') + n) for n in range(26)])
        s, p = p, s
        @lru_cache(None)
        def solve(s_idx, p_idx):


            if p_idx == len(p) and s_idx >= len(s):
                return True
            elif p_idx > len(p):
                return False
            elif s_idx >= len(s):
                return False

            if s[s_idx] in letters and (s_idx == len(s) - 1 or s[s_idx+1] != "*"):
                if p_idx >= len(p):
                    return False

                if s[s_idx] == p[p_idx]:
                    return solve(s_idx+1, p_idx+1)
                else:
                    return False
            elif s[s_idx] in letters and s[s_idx+1] == "*":
                if p_idx == len(p):
                    return solve(s_idx+2, p_idx)
                if s[s_idx] == p[p_idx]:
                    if solve(s_idx+2, p_idx+1) or solve(s_idx, p_idx+1) or solve(s_idx+2, p_idx):
                        return True
                    else:
                        return False
                else:
                    return solve(s_idx+2, p_idx)
            elif s[s_idx] == "." and (s_idx == len(s) - 1 or s[s_idx+1] != "*"):
                return solve(s_idx+1, p_idx+1)
            else:

                if solve(s_idx+2, p_idx+1) or solve(s_idx, p_idx+1) or solve(s_idx+2, p_idx):
                    return True
                else:
                    return False


                    
                    
    
        return solve(0, 0)
