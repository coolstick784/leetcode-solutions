# all the one letters can be palindromes
# fill the the rest from lowest to longest length
# because e.g. for 4 chars vs 2, we'll need 2 pairs for 4 and only 1 for 2
# if it's an odd length, then we only need 1 pair (3 // 2)

# 1, 2, 2, [0 pairs]

class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        lengths = []
        ctr = {}
        for w in words:
            lengths.append(len(w))
            for ch in w:
                ctr[ch] = ctr.get(ch, 0) + 1
        lengths.sort()
        res = 0
        pairs = 0
        for ch in ctr:
            pairs += ctr[ch] // 2

        
        for l in lengths:
            pairs_needed = l // 2
            if pairs >= pairs_needed:
                res += 1
                pairs -= pairs_needed
            else:
                break
        return res
            
