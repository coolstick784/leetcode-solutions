# abc, ab a/b, ac _, aa_, bc_, b a/b _, c__, 
class Solution:
    def addMinimum(self, word: str) -> int:
        res = 0
        idx = 0
        while idx < len(word):
            ch = word[idx]
            if ch == 'a' and (idx == len(word) - 1 or word[idx+1] == 'a'):
                res += 2
                idx += 1
            elif ch == 'a' and idx < len(word) - 2 and word[idx+1] == 'b' and word[idx+2] == 'c':
                idx += 3
            elif ch == 'a' and idx < len(word) - 1 and word[idx+1] == 'b' and (idx == len(word) -2  or word[idx+2] != 'c'):
                res += 1
                idx += 2
            elif ch == 'a' and idx < len(word) - 1 and word[idx+1] == 'c':
                res += 1
                idx += 2
            elif ch == 'b' and idx < len(word) -1 and word[idx+1] == 'c':
                res += 1
                idx += 2
            elif ch == 'b' and (idx == len(word) - 1 or word[idx+1] != 'c'):
                res += 2
                idx += 1
            elif ch == 'c':
                res += 2
                idx += 1
        return res
