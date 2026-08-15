from collections import Counter
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        def isPre(a, b):
            if len(b) != len(a) + 1:
                return False
            b_idx = 0
            changes = 0
            a_idx = 0
            while a_idx < len(a):
                ch = a[a_idx]
                if a_idx >= len(b) or ch != b[b_idx]:
                    changes += 1
                    b_idx += 1
                    
                    if changes >= 2:
                        return False
                else:
                    b_idx += 1
                    a_idx += 1
            return True
        matches = {}
        for idx, word in enumerate(words):
            for idx2, word2 in enumerate(words):
                if isPre(word, word2):
                    matches.setdefault(word, set()).add(idx2)
        
        
        
        @lru_cache(None)
        def solve(idx):
            
            res = 1
            for idx2 in matches.get(words[idx], set()):
                res = max(res, 1 + solve(idx2))
            return res

        out = 1
        for idx, w in enumerate(words):
            out = max(out, solve(idx))
        return out

