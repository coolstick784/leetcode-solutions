class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left_T = 0
        left_F = 0
        cur_max = k

        F_indices = []
        T_indices = []
        num_T = 0
        num_F = 0





 
        # For each substring, get the index of the leftmost T with <= k F's in the substring, or the leftmost F with <= k T's in the substring

        for idx, ch in enumerate(answerKey):
            if ch == 'T':
                T_indices.append(idx)
                num_T += 1
                if num_T >= (k+1):
                    left_F = T_indices[0] + 1
                    del T_indices[0]
            else:
                F_indices.append(idx)
                num_F += 1
                if num_F >= (k+1):
                    left_T = F_indices[0] + 1
                    del F_indices[0]
         
            cur_max = max([idx-left_T+1, idx-left_F + 1, cur_max])


            

        return cur_max
            
            
            
        
