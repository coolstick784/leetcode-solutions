import bisect
class Solution:
    def maxSubstrings(self, word: str) -> int:

        letter_idxs = {}

        for idx, ch in enumerate(word):
            letter_idxs.setdefault(ch, []).append(idx)



        @lru_cache(None)
        def solve(idx):
            if idx >= len(word):
                return 0
            out = 0
            ch = word[idx]
            
            next_idx = bisect.bisect(letter_idxs[ch], idx+2)

            if next_idx < len(letter_idxs[ch]) and letter_idxs[ch][next_idx] >= idx+3:
         
                out = max(out, 1 + solve(letter_idxs[ch][next_idx] + 1))
            out = max(out, solve(idx+1))
            return out


        return solve(0)
