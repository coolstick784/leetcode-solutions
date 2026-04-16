#new, which is set to none for each value
# for each char in s, we set new[idx] tp the index in inicies at that index of s
# return "".join(new)
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new = [None for _ in range(len(s))]
        for idx, ch in enumerate(s):
            new_idx = indices[idx]
            new[new_idx] = ch
        return "".join(new)
