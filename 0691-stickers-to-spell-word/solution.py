from collections import Counter

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        sticker_ctr = {}
        for sticker in stickers:
            sticker_ctr[sticker] = Counter(sticker)
        ctr = Counter(target)
        @lru_cache(None)
        def solve(cur_ctr):
            out = float('inf')
            cur_ctr = dict(cur_ctr)
            if cur_ctr == {}:
                return 0
            for sticker in sticker_ctr:
                new = cur_ctr.copy()
                found = False
                
                for letter in sticker_ctr[sticker]:
                    if new.get(letter, 0) > 0:
                        new[letter] = max(0, new[letter] - sticker_ctr[sticker][letter])
                        if new[letter] == 0:
                            del new[letter]

                        found = True
                if found:
                    new = tuple(sorted(new.items()))
                    out = min(out, 1 + solve(new))
            return out

        new = tuple(sorted(ctr.items()))
        res= solve(new)
        return -1 if res == float('inf') else res
