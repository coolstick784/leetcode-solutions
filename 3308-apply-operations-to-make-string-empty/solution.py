class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        ctr = Counter(s)
        max_ct = max(ctr.values())
        last_idxs = {}
        for idx, ch in enumerate(s):
            last_idxs[ch] = idx
        chars = []
        for ch in ctr:
            if ctr[ch] == max_ct:
                chars.append((last_idxs[ch], ch))
        chars.sort()
        res = [i[1] for i in chars]


        return "".join(res)
