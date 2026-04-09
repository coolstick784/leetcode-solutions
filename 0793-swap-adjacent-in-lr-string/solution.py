# at each character, we want to ask:
# Is this the last character? If so, compare it to the corresponding last character in result. If they're the same, return True. If not, return False
# otherwise, if this character = the corresponding char, move forward 1
# otherwise, if the result char is X, return False
# otherwise, if the result char is L or R, find the next instance of that char and move it back until it's satisified
# so basically if it's XXXXL, we can change that to LXXXX, but if it's e.g. XXXRLX, we can't change that

# L and R can only move backward, X can only move forward
class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        start = list(start)
        idx = 0
        while idx < len(start):
            ch = start[idx]
            corr = result[idx]
            
            if idx == len(start) - 1:
                if ch == corr:
                    return True
                return False
            elif ch == corr:
                idx += 1
                continue
            elif corr == 'X': # if it's X, find the next X. however, only Rs will be allowed in between. if it's a number of Rs then X, swap the first X with the current R
                cur_idx = idx
                while ch == 'R':
                    cur_idx += 1
                    if cur_idx >= len(start):
                        return False
                    ch = start[cur_idx]
                if ch == 'X':
                    start[cur_idx], start[idx] = start[idx], start[cur_idx]
                else:
                    return False
            

            elif corr == 'L': # if it's L, find the next L. same as X but replace X with L and R with X
                cur_idx = idx
                while ch == 'X':
                    cur_idx += 1
                    if cur_idx >= len(start):
                        return False
                    ch = start[cur_idx]
                if ch == 'L':
                    start[cur_idx], start[idx] = start[idx], start[cur_idx]
                else:
                    return False

            elif corr == 'R': # cooked
                return False

            idx += 1
                

                    
                    
        
