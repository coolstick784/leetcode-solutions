class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res = 0
        for idx, word in enumerate(words):
            l1 = len(word)
            for idx2, word2 in enumerate(words[idx+1:]):
                l2 = len(word2)
                word2 = set(word2)
                can_do = True
                for ch in word:
                    if ch in word2:
                        can_do = False
                        break
                if can_do:
                    res = max(res, l1 * l2)
        return res
                
