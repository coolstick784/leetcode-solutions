
class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        pre = {}
        cur_pres = []
        mp = {}
        for ch, r in mappings:
            mp.setdefault(r, set()).add(ch)
        cur = pre
        for idx, ch in enumerate(sub):
            cur.setdefault(ch, {})
            cur = cur[ch]
            if idx == len(sub) -1:
                cur[True] = sub
        
        cur_pres = [pre]
        for idx, ch in enumerate(s):
            poss = mp.get(ch, set())
            poss.add(ch)
            new_pres = []
    
 
            for p_idx, p in enumerate(cur_pres):
                for pos in poss:
                    if pos in p:
                        new_pres.append(p[pos])
                        if True in p[pos]:
                            return True

            new_pres.append(pre)
            cur_pres = new_pres.copy()
            
        return False
