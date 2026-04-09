# get the first non A -- that should be our start
# get the first A after that -- end the one before that
# if all are A, change the last one

class Solution:
    def smallestString(self, s: str) -> str:
        if set(s) == set(['a']):
            return s[:-1] + "z"
        start = 0
        end = 0
        idx = 0
        while idx < len(s):
            ch = s[idx]
            if ch != 'a':
                start = idx
                break
            idx += 1
        while idx < len(s):
            ch = s[idx]
            if ch == 'a':
                end = idx
                break
            idx += 1
        end = idx - 1
        res = ""

        for idx, ch in enumerate(s[:start]):
            res += ch
        for idx, ch in enumerate(s[start:end+1]):
            res += chr(ord(ch) - 1)
        for idx, ch in enumerate(s[end+1:]):
            res += ch
        return res
        


        
