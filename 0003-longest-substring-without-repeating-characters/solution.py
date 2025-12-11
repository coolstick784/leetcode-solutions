class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        cur_str = []
        longest_length = 0
        for idx, c in enumerate(list(s)):
            if c in cur_str:
                idx_c = cur_str.index(c)

                cur_str = cur_str[idx_c + 1:]
            cur_str.append(c)
            cur_length = len(cur_str)
            longest_length = max(cur_length, longest_length)
        return longest_length
