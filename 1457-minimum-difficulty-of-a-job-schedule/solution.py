from collections import deque

class Solution:
    
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        #jobDifficulty = sorted(jobDifficulty)
        #jobDifficulty.reverse()
        @lru_cache(None)
        def solve(start, left, prev):
            
            
            if start >= len(jobDifficulty) and left ==1:

                return prev
            if left == 0 or start >= len(jobDifficulty):
                return float('inf')
            
            out = float('inf')
            # take the job
            out = min(out, solve(start+1, left, max(prev, jobDifficulty[start])))

            # leave the job
            if prev != -float('inf'):
 
                out = min(out, prev + solve(start, left-1, -float('inf')))

            return out

        res= solve(0, d, -float('inf'))
        return res if res != float('inf') else -1
