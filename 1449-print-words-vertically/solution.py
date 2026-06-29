class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        max_len = max([len(w) for w in s])
        res = [[] for _ in range(max_len)]
        idx = 0
        for word in s:
            for idx in range(max_len):
                if idx >= len(word):
                    res[idx].append(" ")
                else:
                    res[idx].append(word[idx])

        return ["".join(w).rstrip() for w in res]
