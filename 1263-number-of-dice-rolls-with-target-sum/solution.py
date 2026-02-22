class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # For each number n 1 to k, add the number of combinations for each other die summing to target - n
        
        # Only keep ones that are possible, so at each n, consider if it can be eventually equal to the target

        res = 0
        ctr = {}
        new_ctr = {}
        for die in range(1, n+1):

            for roll in range(1, k+1):
                if ctr == {}:
                    new_ctr[roll] = 1
                else:
                    for c in ctr:
                        cur = roll + c

                            


                        if cur <= target - (n - die) and cur >= target -( n - die) * k: 
                            new_ctr[cur] = new_ctr.get(cur, 0) + ctr[c]

            ctr = new_ctr.copy()
            new_ctr = {}
        if ctr.get(target, 0) == 0:
            return 0
        return ctr[target] % (10**9 + 7)
                


