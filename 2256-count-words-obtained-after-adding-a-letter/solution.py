class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        start_set = set("".join(sorted(w)) for w in startWords)

        res = 0

        for word in targetWords:
            sorted_word = "".join(sorted(word))

            for i in range(len(sorted_word)):
                candidate = sorted_word[:i] + sorted_word[i+1:]

                if candidate in start_set:
                    res += 1
                    break

        return res
