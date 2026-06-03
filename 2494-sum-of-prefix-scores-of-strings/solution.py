class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        pre = {}
        for word in words:
            cur = pre
            for idx, ch in enumerate(word):
                cur.setdefault(ch, {})

                cur[ch][True] = cur[ch].get(True, 0) + 1
                cur = cur[ch]
        res = []
     
        for word in words:
            cur = pre
            score = 0
            for ch in word:
                
                score += cur[ch].get(True, 0)
                cur = cur[ch]
            
            res.append(score)
        return res


        
