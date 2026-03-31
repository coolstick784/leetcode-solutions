class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        sl = s[0]
        sn = s[1]
        el = s[3]
        en = s[4]
        res = []
        for ch in range(ord(sl), ord(el) + 1):
            for n in range(int(sn), int(en) + 1):
                res.append(chr(ch) + str(n))
        return res


