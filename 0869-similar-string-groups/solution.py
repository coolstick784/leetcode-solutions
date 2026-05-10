class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        matches = {}
        groups = {}

        def find(x):
            if groups[x] != x:
                groups[x] = find(groups[x])
            return groups[x]

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                groups[pb] = pa

        for s in strs:
            groups[s] = s
            matches[s] = [s]
            for idx in range(len(s)):
                ch = s[idx]
                for idx2 in range(idx + 1, len(s)):
                    ch2 = s[idx2]
                    matches[s].append(
                        s[:idx] + ch2 + s[idx + 1:idx2] + ch + s[idx2 + 1:]
                    )

        prev_words = set()

        for s in strs:
            for m in matches[s]:
                if m in prev_words:
                    union(s, m)
            prev_words.add(s)

        return len({find(s) for s in strs})
