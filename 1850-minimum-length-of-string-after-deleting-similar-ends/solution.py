class Solution:
    def minimumLength(self, s: str) -> int:
        self.left = 0
        self.right = len(s) - 1
        def deleteFromLeft():
            ch = s[self.left]
            while s[self.left] == ch and self.left < self.right:
                self.left += 1
        def deleteFromRight():
            ch = s[self.right]
            while s[self.right] == ch and self.right >= self.left:
                self.right -= 1 

        while s[self.left] == s[self.right] and self.left < self.right:

            deleteFromLeft()
            deleteFromRight()
        res = self.right - self.left + 1

        return res
