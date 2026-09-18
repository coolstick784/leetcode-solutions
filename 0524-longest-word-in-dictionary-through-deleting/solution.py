class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        def sub(s1, s2):
            idx = 0
            for i, ch in enumerate(s1):
                if ch == s2[idx]:
                    idx += 1
                if idx == len(s2):
                    return True
            return False


        res = ""
        for w in dictionary:
            if sub(s, w):
                if len(w) > len(res):
                    res = w
                elif len(w) == len(res) and w < res:
                    res = w
        return res
