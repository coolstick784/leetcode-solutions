class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        letters = set([chr(ord('a') + n) for n in range(26)])
        nums = set([str(n) for n in range(10)])
        s = [ch for ch in s if (ch in letters or ch in nums)]
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -=1 
        return True
