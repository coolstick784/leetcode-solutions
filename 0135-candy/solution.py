# if a child <= each neighbor, it gets 1
# child gets max of all neighbors it's greater than + 1 
class Solution:
    def candy(self, ratings: List[int]) -> int:
        

        @lru_cache(None)
        def solve(idx):
          
            if (idx == len(ratings) - 1 or ratings[idx] <= ratings[idx+1]) and (idx == 0 or ratings[idx] <= ratings[idx-1]):
                out = 1

            elif (idx == len(ratings) - 1 or ratings[idx] <= ratings[idx+1]) and (idx != 0 and ratings[idx] > ratings[idx-1]):
                out = solve(idx-1) + 1
           
            elif (idx != len(ratings) - 1 and ratings[idx] > ratings[idx+1]) and (idx == 0 or ratings[idx] <= ratings[idx-1]):
                out = solve(idx+1) + 1
            
            else:
                out = max(solve(idx-1), solve(idx+1)) + 1
            
         
            return out
        solve(0)
        return sum([solve(idx) for idx, n in enumerate(ratings)])
        
