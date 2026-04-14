# we want to know, given a list of strings, and the start index of the first column, which column indices do we need to delete?
# if all are < the next, or all are "", return set()
# if even 1 is < the previous, add that column index and add the union of all others starting with ""
# if they're in order but some are equal, return the union of our current resolution as well as the union of all other equivalent starts

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
      
        cur_idx = 0
  
        equal = [[n for n in range(len(strs))]]
        res = 0
        remove = False


        while equal and cur_idx < len(strs[0]):
            
            new_equal = []
            remove = False
            
            for grp in equal:
                prev_n = -2
                cur_grp = []
                for idx in grp:
                    s = strs[idx]
                    next_ch = s[cur_idx]

                    cur_n = ord(s[cur_idx])  - ord('a')
                    if cur_n < prev_n:
                        remove = True
                        break
                    elif cur_n == prev_n:
                        if not cur_grp:
                            cur_grp = [prev_idx]
                        cur_grp.append(idx)
                    else:
                        if cur_grp:
                            new_equal.append(cur_grp)
                        cur_grp = []
                    prev_n = cur_n
                    prev_idx = idx
                if cur_grp:
                    new_equal.append(cur_grp)

                if remove:
                    break
            cur_idx += 1
            if remove:
                remove = False
                res += 1
            else:
                equal = new_equal.copy()


        return res

        
