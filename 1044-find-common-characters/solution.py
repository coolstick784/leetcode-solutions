class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ctr = Counter(words[0])
        for word in words[1:]:
            cur = Counter(word)
            for ch in ctr:
                ctr[ch] = min(ctr[ch], cur.get(ch, 0))
        res = []
        for ch in ctr:
            for _ in range(ctr[ch]):
                res.append(ch)
        return res
