class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:

        s_groups = []
        res = 0
        for idx, ch in enumerate(s):
            ct = 0
            if idx > 0 and ch == s[idx-1]:
                _, ct = s_groups.pop()
            s_groups.append((ch, ct + 1))
        all_w = []
        for w in words:
            g = []
            for idx, ch in enumerate(w):
                ct = 0
                if idx > 0 and ch == w[idx-1]:
                    _, ct = g.pop()
                g.append((ch, ct + 1))
            all_w.append(g)
        for g in all_w:
            print(g)
            if len(g) != len(s_groups):
                continue
            equal = True
            for idx, (ch, ct) in enumerate(g):
                if ch != s_groups[idx][0]:
                    equal = False
                    break
                s_ct = s_groups[idx][1]
                if ct == s_ct:
                    continue
                if ct > s_ct:
                    equal = False
                    break
                if s_ct < 3:
                    equal = False
                    break
            if equal:
                res += 1
        return res
            

                

