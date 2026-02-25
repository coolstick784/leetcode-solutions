class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # 1. Get the number of possibilites that are still possible to reach the target, with their counts for die j - 1
        # Add 1 to each possibily for each i from 1 to k 
        
        cur_poss = {0:1}
        next_poss = {}
        for die in range(1, n+1):

            next_poss = {}
            #possible_min = target - 6*(n - die)
            #possible_max = target - n - die
            for num in cur_poss:
                ct = cur_poss[num]
                for j in range(1, k+1):
                    next_poss[num+j] = next_poss.get(num+j, 0) + ct
                    
                    
            
            
            cur_poss = next_poss.copy()
        if cur_poss.get(target, 0) == 0:
            return 0
        return cur_poss[target] % (10**9+7)
        
        
