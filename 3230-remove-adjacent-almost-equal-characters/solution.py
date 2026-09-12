class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        res = 0
        changed = False
        for idx, ch in enumerate(word[:-1]):
            if changed:
                changed = False
                continue
            if abs(ord(ch) - ord(word[idx+1])) <= 1:
                changed = True
                res += 1
        return res
