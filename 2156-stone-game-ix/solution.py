# [1, 1, 1, 1, 2, 2, 0]
# 2 -> 2 -> 1 
# if there are only 2s and 1s, and we start at 2, we go 2->1->2->1...
# if there more 2s than 1s, p1 wins
# if there more 1s than 2s, p2 wins
# if there are only 2s and 1s, and we start at 1, then if there are more 1s than 2s, p1 wins
# otherwise, if there are more 2s than 1s, p2 wins
# if there are only 0s, bob wins
# if there are an equal amount of 2s and 1s, and an even amount of 0s, alice wins
# if there are an equal amount of 2s and 1s, and an odd amount of 0s, bob wins
# alice needs 2 1s left starting at 1, or 2 2s left starting at 2
# if abs(num 1s - num2s) >= 3 alice wins no matter what
# if abs(num 1s - num 2s) == 1 and there is an odd amount of 0s, bob wins
# if abs(num 1s - num 2s) == 1 and there is an even amount of 0s, alice wins
# if abs(num 1s - num 2s) == 2 and there is an even amount of 0s, alice wins
# if abs(num 1s - num 2s) == 2 and there is an odd amount of 0s, bob wins

class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        new = []
        if len(stones) == 1:
            return False
        
        for s in stones:
            new.append(s % 3)
        
        ctr = Counter(new)
        def solve(c1, c2, start):
            if c1 < 0 or c2 < 0:
                return False
            if c1 == 0 and c2 == 0:
                return False
            if start == 1:
                if c1 >= c2:
                    return False
                else:
                    return True
            else:
                if c2 >= c1:
                    return False
                else:
                    return True
            
        
        if ctr[0] % 2 == 0:
            return solve(ctr[1]-1, ctr[2], 1) or solve(ctr[1], ctr[2]-1, 2)
        else:
            return solve(ctr[1]-2, ctr[2], 2) or solve(ctr[1], ctr[2]-2, 1)
