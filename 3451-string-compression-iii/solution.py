class Solution:
    def compressedString(self, word: str) -> str:
        res = []
        cur_ct  = 0
        cur_ch = None
        for idx, ch in enumerate(word):
            if idx == 0:
                cur_ch = ch
                cur_ct = 0
            if cur_ct == 9 or (cur_ch and cur_ch != ch):
                res.append(str(cur_ct) + cur_ch)
                cur_ch = ch
                cur_ct = 1
            else:
                cur_ct += 1
        
        res.append(str(cur_ct) + cur_ch)
        cur_ch = ch
        cur_ct = 1

        return "".join(res)
