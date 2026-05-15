class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        max_repeating = [0 for _ in s]
        max_non_repeating = [0 for _ in s]
        for idx, ch in enumerate(s):
            if idx == 0:
                max_non_repeating[idx] = 1
                continue
            if s[idx] == s[idx-1]:
                max_repeating[idx] = max(2, max_non_repeating[idx-1] + 1)
            else:
                max_non_repeating[idx] = max(2, max_non_repeating[idx-1] + 1)
                max_repeating[idx] = max(2, max_repeating[idx-1] + 1)
        

        return max(max(max_repeating), max(max_non_repeating))
