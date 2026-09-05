class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        w1 = sentence1.split()
        w2 = sentence2.split()
        if len(w1) == len(w2):
            return w1 == w2
        if len(w1) > len(w2):
            w1, w2 = w2, w1

        @lru_cache(None)
        def solve(w1_idx, w2_idx, used, using):
            if w1_idx == len(w1) and w2_idx == len(w2):
                return True
            if w1_idx == len(w1) and (not used or using):
                return True
            if w1_idx >= len(w1) or w2_idx >= len(w2):
                return False
            word1 = w1[w1_idx]
            word2 = w2[w2_idx]
            print(w1_idx, w2_idx)

            if not used or using:
                if solve(w1_idx, w2_idx+1, True, True):
                    return True
            if word1 == word2 and solve(w1_idx+1, w2_idx+1, used, False):
                return True
            return False
        return solve(0, 0, False, False)
