class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = 0
        def diffOne(w1, w2):
            if len(w1) != len(w2):
                return False
            diffs = 0
            for idx, ch in enumerate(w1):
                if ch != w2[idx]:
                    diffs += 1
            return diffs == 1
        dp = {}
        next_idx = {}
        best_idx = None
        
        for idx in range(len(words)-1, -1, -1):
            word = words[idx]
            out = 1
            next_idx[idx] = None
            
            best_l = None
            for new_idx in range(idx+1, len(words)):
                comp = words[new_idx]
                prev_best = dp[new_idx]
                if groups[new_idx] != groups[idx] and diffOne(word, comp):
                    if 1 + prev_best > out:
                        out = 1 + prev_best
                        next_idx[idx] = new_idx
                
                

            
            dp[idx] = out
            if out > res:
                res = out
                best_idx = idx
        
                
        fin = []
        
        cur = best_idx
        while cur is not None:
            
            fin.append(words[cur])
            cur = next_idx[cur]
        return fin

