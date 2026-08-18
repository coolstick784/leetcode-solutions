class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        @lru_cache(None)
        def solve(s1_idx, s2_idx):
            if s1_idx > len(str1) or s2_idx > len(str2):
                return float('inf')
            if s1_idx == len(str1) and s2_idx == len(str2):
                return 0
            if s1_idx == len(str1):
                return 1 + solve(s1_idx, s2_idx+1)
            if s2_idx == len(str2):
                return 1 + solve(s1_idx+1, s2_idx)
            s1 = str1[s1_idx]
            s2 = str2[s2_idx]
            out = float('inf')
            if s1 == s2:
                out = min(out, 1+solve(s1_idx+1, s2_idx+1))
            out = min(out, 1 + solve(s1_idx+1, s2_idx), 1 + solve(s1_idx, s2_idx+1))
            return out


        l = solve(0, 0)
        cur = (0, 0)
        res = []
        for _ in range(l):
            p1 = float('inf')
            s1 = cur[0] 
            s2 = cur[1]
            if s1 < len(str1) and s2 < len(str2) and str1[s1] == str2[s2]:
                p1 = solve(s1+1, s2+1)
            p2 = solve(s1+1, s2)
            p3 = solve(s1, s2+1)
            if p1 == min(p1, p2, p3):
                cur = (s1+1, s2+1)
                res.append(str1[s1])
            elif p2 <= p3:
                cur = (s1+1, s2)
                res.append(str1[s1])
            else:
                cur = (s1, s2+1)
                res.append(str2[s2])


        return res
            

