# for each left, find the min right, then add the rest
from collections import Counter
class Solution:

    def validSubstringCount(self, word1: str, word2: str) -> int:
        left = 0
        right = 0
        res = 0
        ctr = Counter(word2)
        rem = len(word2)
        while left < len(word1):
            while right < len(word1) and rem > 0:
                r = word1[right]
             
                if r in ctr:
                    if ctr[r] > 0:
                        rem -= 1
                    ctr[r] -= 1
                right += 1
            
            if rem == 0:
                res += len(word1) - right + 1
            l = word1[left]
            if l in ctr:
                ctr[l] += 1
                if ctr[l] > 0:
                    rem += 1
            left += 1
        return res
            

