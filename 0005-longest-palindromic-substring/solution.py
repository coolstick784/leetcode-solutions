class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        max_len = 0
        for idx, ch in enumerate(s):
            left = idx
            right = idx
            while left > 0 and right < len(s)-1 and s[left-1] == s[right+1]:
                left -= 1
                right += 1
            cur_len = right - left + 1
            if cur_len > max_len:
                max_len = cur_len
                res = s[left:right+1]

        for idx, ch in enumerate(s[:-1]):
            left = idx
            right = idx+1
            if s[left] != s[right]:
                continue
            while left > 0 and right < len(s)-1 and s[left-1] == s[right+1]:
                left -= 1
                right += 1
            cur_len = right - left + 1
            if cur_len > max_len:
                max_len = cur_len
                res = s[left:right+1]
        return res

