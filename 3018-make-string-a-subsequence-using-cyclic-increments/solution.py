class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        
        str1_left = 0
        str2_left = 0
        while str1_left < len(str1):
            str2_ch = str2[str2_left]
            old = str1[str1_left]
            if old != 'z':
                new = chr(ord(old) + 1)
            else:
                new = 'a'
            if str2_ch == old or str2_ch == new:
                str2_left += 1
                str1_left += 1
            else:
                str1_left += 1
            if str2_left == len(str2):
                return True
        return False
