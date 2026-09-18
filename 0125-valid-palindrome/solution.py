class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = s.lower()
        letters = [chr(ch) for ch in range(ord('a'), ord('a') + 26)]
        numbers = [str(n) for n in range(10)]
        clean = [ch for ch in clean if ch in letters or ch in numbers]
        return clean == clean[::-1]
