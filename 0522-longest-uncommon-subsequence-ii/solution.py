class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        res = -1
        def isSub(s1, s2):
          
            if len(s1) > len(s2):
                return False
            i1 = 0
            i2 = 0
            while i2 < len(s2):
                if s2[i2] == s1[i1]:
                    i1 += 1
                i2 += 1
                if i1 == len(s1):
                    return True
            return False
        for idx1, s1 in enumerate(strs):
            found = False
            for idx2, s2 in enumerate(strs):
                if idx1 == idx2:
                    continue
                if isSub(s1, s2):
                    print(s1, 'found', s2)
                    found = True
            if not found:
                res = max(res, len(s1))
        return res
                    
