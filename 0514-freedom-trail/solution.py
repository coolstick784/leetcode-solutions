class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        
        letters = {}
        for idx, ch in enumerate(ring):
            letters.setdefault(ch, []).append(idx)
        letters[None] = [0]
        best = {0: 0}

        prev_ch = None
        for idx, ch in enumerate(key):
            print("best", best)
            prev_idxs = letters[prev_ch]
            cur_idxs = letters[ch]
            prev_best = [(i, best[i]) for i in prev_idxs]
            for i in cur_idxs:
                best[i] = float('inf')
            for p, b in prev_best:
                for c in cur_idxs:
                    if c > p:
                        best[c] = min(best[c], c-p+1+b, p + 1 +  (len(ring)-1-c) + 1+b)
                    else:
                        best[c] = min(best[c], p-c+1 + b, (len(ring)-1-p) + c + 1 + 1 + b)
            prev_ch = ch
        
        return min([best[idx] for idx in letters[key[-1]]])
