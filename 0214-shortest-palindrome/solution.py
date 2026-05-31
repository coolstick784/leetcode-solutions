class Solution:
    def shortestPalindrome(self, s: str) -> str:
        for end in range(len(s), -1, -1):
            prefix = s[:end]

            if prefix == prefix[::-1]:
                suffix = s[end:]
                return suffix[::-1] + s
