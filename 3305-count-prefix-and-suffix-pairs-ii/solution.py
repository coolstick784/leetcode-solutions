class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        pre = {}
        suf = {}
        ctr = {}
        res = 0
        for idx in range(len(words)-1, -1, -1):
            cword = words[idx]
            cur = pre
            for ch in cword:
                cur = cur.get(ch, {})
                if cur == {}:
                    break

            out = cur.get(True, set())
            cur = suf
            for ch in cword[::-1]:
                cur = cur.get(ch, {})
                if cur == {}:
                    break
            for word in cur.get(True, set()):
                if word in out:
                    res += ctr[word]


            cur = pre
            for ch in cword:
                cur.setdefault(ch, {})
                cur[ch].setdefault(True, set()).add(cword)
                cur = cur[ch]
            cur = suf
            for ch in cword[::-1]:
                cur.setdefault(ch, {})
                cur[ch].setdefault(True, set()).add(cword)
                cur = cur[ch]
            ctr[cword] = ctr.get(cword, 0) + 1
        return res
