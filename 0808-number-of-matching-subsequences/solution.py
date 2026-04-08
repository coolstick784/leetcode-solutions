from collections import defaultdict

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        starts = defaultdict(list)
        res = 0

        for word in words:
            starts[word[0]].append((word, 0))

        for ch in s:
            old_words = starts[ch]
            starts[ch] = []

            for word, idx in old_words:
                idx += 1
                if idx == len(word):
                    res += 1
                else:
                    starts[word[idx]].append((word, idx))

        return res
