class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ctr = {}
        for ch in chars:
            ctr[ch] = ctr.get(ch, 0) + 1
        def wordCanBeMade(word):
            cur_ctr = ctr.copy()
            for ch in word:
                cur_ctr[ch] = cur_ctr.get(ch, 0) - 1
                if cur_ctr[ch] < 0:
                    return False
            return True
            
        res = 0
        for word in words:
            if wordCanBeMade(word):
                res += len(word)
        return res
