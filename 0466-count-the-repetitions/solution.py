from collections import Counter
class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:

 
        @lru_cache(None)
        def solve(start_idx):
            cur_s1 = s1[start_idx:] + s1 * len(s2)
            idx = 0
            s2_idx = 0
            while s2_idx < len(s2) and idx < len(cur_s1):
                if cur_s1[idx] == s2[s2_idx]:
                    s2_idx += 1
                idx += 1

            if s2_idx != len(s2):
                return (float('inf'), float('inf'), float('inf'))
            rem = len(s1) - start_idx
            
            if idx < rem:
                n_iters = 0
                new_idx = start_idx + idx

            else:
                n_iters = 1 + math.floor((idx-rem) / len(s1))
                new_idx = (idx - rem) % len(s1)
            

            return (idx, n_iters, new_idx)

        
        mp = {}
        for idx in range(len(s1)):
            mp[idx] = solve(idx)


        if mp[0][0] == float('inf'):
            return 0
        
        loops = {} # idx: (n_iters to loop, loop idx, length of loop)
        explored = {}
        iters = [(0, 0)]
        cur = 0
        cur_iters = 0
        idx = 0
  
        while cur not in explored:
   
            
            explored[cur] = idx
            
            cur = mp[cur][2]
            cur_iters = mp[cur][1]
            iters.append((cur, cur_iters))
            idx += 1
     
            
        

        dist_to_loop = 0
        loop_length = 0
        iters_to_loop = 0
        iters_per_loop = 0
        in_loop = False

        for idx, cur_iters in iters:
            if not in_loop and idx != cur:
                iters_to_loop += cur_iters
                dist_to_loop += 1
            else:
                if in_loop:
                    iters_per_loop += cur_iters
                    loop_length += 1
                in_loop = True
                

        




        # med = n2 * sol
        # dist to loop is the number of s2's we can get before looping
        # loop length is the number of s2's per loop
        # iters to loop is the number of s1's we need to get to the lo0op
        # iters per loop is the number of s1's in each loop

    
        n_iters = 1
        cur = 0
        sol = 0 

        print("dist to loop", dist_to_loop, "iters per loop", iters_per_loop, "iters", iters, "loop length", loop_length)
    
        while dist_to_loop > 0:
            _, cur_iters, cur = mp[cur]
            
            if n_iters + cur_iters <= n1:
                n_iters += cur_iters
                sol += 1
            else:
                break

            
            dist_to_loop -= 1
        
        while (n_iters + iters_per_loop <= n1) or (n_iters+iters_per_loop == n1+1 and cur == 0):
            n_iters += iters_per_loop
            sol += loop_length
        
       
        while (n_iters + mp[cur][1] <= n1):
            _, cur_iters, cur = mp[cur]
            n_iters += cur_iters
            sol += 1
        print("sol", sol)
        return sol // n2







