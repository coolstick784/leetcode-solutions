class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        words = [w for w in words if w.strip() != ""]
        return len(words[-1])
        
