class Solution:
    def customSortString(self, order: str, s: str) -> str:
        key = {}
        chs = set(order)
        ctr = 1
        for ch in order:
            key[ctr] = ch
            ctr += 1
        res = ""
        end = ""
        for n in range(1, 27):
            for ch in s:
                if ch == key.get(n, ""):
                    res += ch
        for ch in s:
            if ch not in chs:
                end += ch
        return res + end 
        
                    
        
        
