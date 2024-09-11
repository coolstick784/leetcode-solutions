class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        out = len(words)

        for word in words:
            for char in word:
                if char not in allowed:
                    out -= 1
                    break
        return out
