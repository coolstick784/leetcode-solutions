class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        base = False
        counts = [0] * len(set(s))
        letters = set(s)
        letters = list(letters)
        counts2 = [0] * len(set(t))
        letters2 = set(t)
        letters2 = list(letters2)
        letters.sort()
        letters2.sort()
        for i in s:
            index = letters.index(i)
            counts[index] += 1
        
        for i in t:
            index = letters2.index(i)
            counts2[index] += 1
        
        if (counts == counts2) and (letters == letters2):
            base = True
        return base
