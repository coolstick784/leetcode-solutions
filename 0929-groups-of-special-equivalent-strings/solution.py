class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        groups = {}
        for idx, w in enumerate(words):
            even = []
            odd = []
            for i, ch in enumerate(w):
                if i % 2 == 0:
                    even.append(ch)
                else:
                    odd.append(ch)
            even = "".join(sorted(even))
            odd = "".join(sorted(odd))
            groups.setdefault(even, set()).add(odd)

        return sum([len(groups[group]) for group in groups])
